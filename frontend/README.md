# Stock Tracker Frontend

A TypeScript-based frontend application for displaying stocks and their prices retrieved from the backend API.

## Features

- Fetches all stocks from the backend `/api/stocks` endpoint
- Displays stocks in a clean, responsive table
- Real-time price display with proper formatting
- Error handling and empty state management
- Modern, gradient-based UI design

## Project Structure

```
frontend/
├── src/
│   ├── main.ts          # Main TypeScript application logic
│   └── styles.css       # Styling for the application
├── index.html           # HTML template
├── package.json         # Node dependencies
├── tsconfig.json        # TypeScript configuration
├── tsconfig.node.json   # TypeScript Node configuration
└── vite.config.ts       # Vite configuration
```

## Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Development

Start the development server with hot module replacement:

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

The Vite dev server is configured to proxy API requests to `http://localhost:5000` (the Flask backend).

## Building

To build the application for production:

```bash
npm run build
```

This will compile TypeScript and create an optimized build in the `dist/` directory.

## API Integration

The frontend expects the backend to provide a `/api/stocks` endpoint that returns:

```json
{
  "stocks": [
    {
      "symbol": "AAPL",
      "price": "150.25"
    },
    {
      "symbol": "GOOGL",
      "price": "2800.50"
    }
  ]
}
```

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Modern browsers with ES2020 support
