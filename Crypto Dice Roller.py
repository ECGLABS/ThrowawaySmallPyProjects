import tkinter as tk
import random
import requests

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

def roll_crypto():
    roll = random.randint (1, 6)
    chosen = cryptos[roll]
    label.config(text=f"You Rolled for {roll}!\nCrypto: {chosen}")
    name, api_id = cryptos[roll]
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={api_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data[api_id]['usd']
    label.config(text=f"You rolled a {roll}!\n{name} is worth ${price:,}")

button = tk.Button(window, text="TIME TO GAMBA", command=roll_crypto)
button.pack()


window.mainloop()
