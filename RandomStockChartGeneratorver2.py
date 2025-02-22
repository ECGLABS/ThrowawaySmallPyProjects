import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def generate_random_stock_data(days=100, volatility=0.02, initial_price=100):
    # Generate daily returns using random walk
    returns = np.random.normal(loc=0.0001, scale=volatility, size=days)
    # Calculate price series
    price_data = initial_price * (1 + returns).cumprod()

    # Generate dates for x-axis
    end_date = datetime.now()
    dates = [end_date - timedelta(days=x) for x in range(days)]
    dates.reverse()

    return dates, price_data


def plot_stock_chart():
    # Create figure and axis
    plt.figure(figsize=(12, 6))

    # Generate random data
    dates, prices = generate_random_stock_data()

    # Plot the line
    plt.plot(dates, prices, color='#0066cc', linewidth=2)

    # Customize the chart
    plt.title('Random Stock Price Movement', fontsize=14, pad=15)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price ($)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    plot_stock_chart() 
