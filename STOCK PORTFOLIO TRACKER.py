import requests
import json

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        """Add a stock to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'price': 0.0}

    def remove_stock(self, symbol):
        """Remove a stock from the portfolio."""
        if symbol in self.portfolio:
            del self.portfolio[symbol]
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def update_prices(self, api_key):
        """Fetch and update stock prices using Finnhub API."""
        base_url = "https://finnhub.io/api/v1/quote"
        for symbol in self.portfolio.keys():
            params = {
                "symbol": symbol,
                "token": api_key
            }
            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                try:
                    price = float(data["c"])  # 'c' represents the current price in Finnhub's response
                    self.portfolio[symbol]['price'] = price
                except KeyError:
                    print(f"Error fetching data for {symbol}.")
            else:
                print(f"Failed to fetch stock price for {symbol}. HTTP Status: {response.status_code}")

    def calculate_portfolio_value(self):
        """Calculate the total value of the portfolio."""
        total_value = 0.0
        for stock in self.portfolio.values():
            total_value += stock['shares'] * stock['price']
        return total_value

    def display_portfolio(self):
        """Display the current portfolio."""
        print("\nPortfolio:")
        for symbol, info in self.portfolio.items():
            print(f"{symbol}: {info['shares']} shares @ ${info['price']:.2f} each")
        print(f"Total Portfolio Value: ${self.calculate_portfolio_value():.2f}\n")

    def save_portfolio_to_file(self, filename="portfolio.json"):
        """Save the current portfolio to a JSON file."""
        with open(filename, "w") as file:
            json.dump(self.portfolio, file, indent=4)
        print(f"Portfolio saved to {filename}.")

    def load_portfolio_from_file(self, filename="portfolio.json"):
        """Load a portfolio from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.portfolio = json.load(file)
            print(f"Portfolio loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

# Main Menu Logic
def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Performance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL, MSFT, TSLA): ")
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)

        elif choice == '2':
            symbol = input("Enter stock symbol to remove (e.g., AAPL, MSFT, TSLA): ")
            portfolio.remove_stock(symbol)

        elif choice == '3':
            api_key = input("Enter your Finnhub API key: ")
            portfolio.update_prices(api_key)
            portfolio.display_portfolio()

        elif choice == '4':
            portfolio.save_portfolio_to_file()
            print("Exiting Stock Portfolio Tracker.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()









