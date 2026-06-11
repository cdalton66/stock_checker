from decimal import Decimal, InvalidOperation

import config
from sqlalchemy import Column, Numeric, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

class StockQuote(Base):
    __tablename__ = "stock_quotes"

    symbol = Column(String(16), primary_key=True, nullable=False)
    price = Column(Numeric(18, 8), nullable=False)


def init_db():
    """Create the stock_quotes table if it does not already exist."""
    Base.metadata.create_all(bind=engine)


def upsert_stock_quote(symbol: str, price):
    """Insert or update a stock quote record."""
    if not symbol or not symbol.strip():
        raise ValueError("Stock symbol is required for database storage.")

    try:
        price_value = Decimal(str(price))
    except (InvalidOperation, TypeError) as exc:
        raise ValueError(f"Invalid price value: {price}") from exc

    symbol = symbol.strip().upper()
    with SessionLocal() as session:
        quote = session.get(StockQuote, symbol)
        if quote is None:
            quote = StockQuote(symbol=symbol, price=price_value)
            session.add(quote)
        else:
            quote.price = price_value
        session.commit()
    return quote
