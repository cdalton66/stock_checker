-- Create the stocks database
CREATE DATABASE IF NOT EXISTS stocks;

-- Use the stocks database
USE stocks;

-- Create the stock_quotes table
CREATE TABLE IF NOT EXISTS stock_quotes (
    symbol VARCHAR(16) PRIMARY KEY NOT NULL,
    price DECIMAL(18, 8) NOT NULL
);
