import random
import matplotlib.pyplot as plt

def generate_stock_chart(days):
    # Generate random stock prices
    prices = [random.uniform(50, 200) for _ in range(days)]

    # Generate random volume data
    volume = [random.randint(100000, 1000000) for _ in range(days)]

    # Plot the stock chart
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(prices)
    plt.title('Stock Price')
    plt.ylabel('Price')
    plt.grid(True)

    # Plot the volume chart
    plt.subplot(2, 1, 2)
    plt.plot(volume, color='g')
    plt.title('Volume')
    plt.xlabel('Days')
    plt.ylabel('Volume')
    plt.grid(True)

    # Adjust subplots spacing
    plt.subplots_adjust(hspace=0.4)

    # Display the chart
    plt.show()

# Generate a random stock chart with 30 days of data
generate_stock_chart(30)
