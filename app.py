from flask import Flask, jsonify
import requests
from sqlalchemy.exc import SQLAlchemyError
import config
import db
import warnings

# Suppress NotOpenSSLWarning for LibreSSL
warnings.filterwarnings('ignore', message='.*NotOpenSSLWarning.*')

app = Flask(__name__)
try:
    db.init_db()
except Exception as exc:
    warnings.warn(f"Database initialization failed: {exc}")


def getStock(symbol):
    """Fetch stock price from Alpha Vantage API"""
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": config.API_KEY,
    }
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()
    
    # Check if Global Quote data exists
    if "Global Quote" not in data:
        raise ValueError(f"Invalid stock symbol: {symbol}")
    global_quote = data["Global Quote"]
    # Check if quote data is empty
    if not global_quote or "05. price" not in global_quote:
        raise ValueError(f"Invalid stock symbol: {symbol}")
    price = global_quote["05. price"]
    # Check if price is empty
    if not price:
        raise ValueError(f"Invalid stock symbol: {symbol}")
    return price


@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_price(symbol):
    """
    API endpoint to get stock price
    
    Args:
        symbol: Stock symbol (e.g., AAPL, GOOGL)
    
    Returns:
        JSON response with stock symbol and price
    """
    try:
        symbol = symbol.strip().upper()
        
        if not symbol:
            return jsonify({
                "error": "Stock symbol cannot be empty."
            }), 400
        
        price = getStock(symbol)
        try:
            db.upsert_stock_quote(symbol, price)
        except SQLAlchemyError as exc:
            warnings.warn(f"Database write failed: {exc}")

        return jsonify({
            "symbol": symbol,
            "price": price
        }), 200
    
    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 404
    except Exception as e:
        return jsonify({
            "error": f"Error retrieving stock data: {str(e)}"
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
