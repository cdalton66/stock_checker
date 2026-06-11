# Docker Setup for Stock Tracker Backend

This is the backend service for the Stock Tracker application. It uses Flask to expose REST APIs for fetching and storing stock prices.

## Environment Variables

- `API_KEY`: Alpha Vantage API key (required)
- `MYSQL_HOST`: MySQL database host (default: host.docker.internal)
- `MYSQL_PORT`: MySQL database port (default: 3306)
- `MYSQL_DB`: Database name (default: stocks)
- `MYSQL_USER`: Database user (default: root)
- `MYSQL_PASSWORD`: Database password (default: empty)

## Building the Docker Image

```bash
docker build -t stock-tracker-backend .
```

## Running the Container

```bash
docker run -p 5001:5000 \
  -e API_KEY=your_api_key \
  -e MYSQL_HOST=localhost \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=password \
  stock-tracker-backend
```

## API Endpoints

- `GET /health` - Health check
- `GET /api/stock/<symbol>` - Get stock price by symbol (fetches from Alpha Vantage)
- `GET /api/stocks` - Get all stocks from database
