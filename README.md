# Stock Quote Flask App

A small Flask service that retrieves stock prices from Alpha Vantage and stores them in MySQL.

## Features

- `/api/stock/<symbol>`: fetches the latest stock price from Alpha Vantage
- Persists stock symbol and price to MySQL
- Docker-ready application with local MySQL host support

## Requirements

- Python 3.11+
- Local MySQL server running on `localhost:3306`
- Alpha Vantage API key

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set environment variables:

```bash
export API_KEY=your_alpha_vantage_key
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DB=stocks
```

## Run locally

```bash
python app.py
```

## Run with Docker Compose

```bash
docker compose up --build
```

The container connects to the local MySQL server using `host.docker.internal` by default.

## GitHub Actions

A basic workflow is included at `.github/workflows/python-app.yml` to install dependencies and run a syntax check.
