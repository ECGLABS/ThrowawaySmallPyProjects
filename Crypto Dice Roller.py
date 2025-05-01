import tkinter as tk
import random
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#tkinter window generation code
window = tk.Tk()
window.title("Crypto Roller")
window.geometry("400x400")
label = tk.Label(window, text=" Roll to see a random crypto", font=("Arial", 14))
label.pack(pady=20)

#Creates the roll  function
def roll_crypto():
    label.config(text="Rolling... (we'll add results soon)")


#Define Crypto List with a dictionary
cryptos ={
    1:("Bitcoin", "bitcoin"),
    2:("Ethereum", "ethereum"),
    3:("Ripple", "ripple"),
    4:("(Dogecoin", "dogecoin"),
    5:("Hex", "hex"),
    6:("Pulsechain" , "pulsechain"),
    }

chart_canvas = None

def roll_crypto():
    global chart_canvas
    roll = random.randint (1, 6)
    chosen = cryptos[roll]
    label.config(text=f"You Rolled for {roll}!\nCrypto: {chosen}")
    name, api_id = cryptos[roll]
    history_url = f"https://api.coingecko.com/api/v3/coins/{api_id}/market_chart?vs_currency=usd&days=7"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={api_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data[api_id]['usd']
    label.config(text=f"You rolled a {roll}!\n{name} is worth ${price:,}")
    history_response = requests.get(history_url)
    history_data = history_response.json()

    prices = [point[1] for point in history_data['prices']]

    if chart_canvas is not None:
        chart_canvas.get_tk_widget().destroy()


    fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
    ax.plot(prices, label=f"{name} - 7 Day History", color="blue")
    ax.set_ylabel("Price (USD)")
    ax.set_xlabel("Time")
    ax.legend()

    chart_canvas = FigureCanvasTkAgg(fig, master=window)
    chart_canvas.draw()
    chart_canvas.get_tk_widget().pack()


button = tk.Button(window, text="TIME TO GAMBA", command=roll_crypto)
button.pack()


window.mainloop()
