interface Stock {
  symbol: string;
  price: string;
}

interface ApiResponse {
  stocks: Stock[];
  error?: string;
}

const API_BASE_URL = '/api';

async function fetchStocks(): Promise<Stock[]> {
  try {
    const response = await fetch(`${API_BASE_URL}/stocks`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data: ApiResponse = await response.json();
    
    if (data.error) {
      throw new Error(data.error);
    }
    
    return data.stocks || [];
  } catch (error) {
    console.error('Error fetching stocks:', error);
    throw error;
  }
}

function displayStocks(stocks: Stock[]): void {
  const loadingDiv = document.getElementById('loading');
  const errorDiv = document.getElementById('error');
  const table = document.getElementById('stocks-table');
  const tbody = document.getElementById('stocks-tbody');
  const emptyState = document.getElementById('empty');

  if (!table || !tbody || !loadingDiv || !errorDiv || !emptyState) {
    console.error('Required DOM elements not found');
    return;
  }

  // Hide all sections
  loadingDiv.style.display = 'none';
  errorDiv.style.display = 'none';
  table.style.display = 'none';
  emptyState.style.display = 'none';

  if (stocks.length === 0) {
    emptyState.style.display = 'block';
    return;
  }

  // Clear existing rows
  tbody.innerHTML = '';

  // Add rows for each stock
  stocks.forEach((stock) => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td class="symbol">${escapeHtml(stock.symbol)}</td>
      <td class="price">$${formatPrice(stock.price)}</td>
    `;
    tbody.appendChild(row);
  });

  table.style.display = 'table';
}

function displayError(error: string): void {
  const loadingDiv = document.getElementById('loading');
  const errorDiv = document.getElementById('error');
  const table = document.getElementById('stocks-table');
  const emptyState = document.getElementById('empty');
  const errorMessage = document.getElementById('error-message');

  if (!loadingDiv || !errorDiv || !table || !emptyState || !errorMessage) {
    console.error('Required DOM elements not found');
    return;
  }

  loadingDiv.style.display = 'none';
  table.style.display = 'none';
  emptyState.style.display = 'none';
  
  errorMessage.textContent = error;
  errorDiv.style.display = 'block';
}

function formatPrice(price: string): string {
  try {
    const numPrice = parseFloat(price);
    return numPrice.toFixed(2);
  } catch {
    return price;
  }
}

function escapeHtml(text: string): string {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

async function initializeApp(): Promise<void> {
  try {
    const stocks = await fetchStocks();
    displayStocks(stocks);
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown error occurred';
    displayError(`Failed to load stocks: ${errorMessage}`);
  }
}

// Initialize the app when the DOM is ready
document.addEventListener('DOMContentLoaded', initializeApp);
