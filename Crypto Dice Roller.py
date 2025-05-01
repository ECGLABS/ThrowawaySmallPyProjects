import tkinter as tk
import random

#tkinter window generation code
window = tk.Tk()
window.title("Crypto Roller")
window.geometry("400x400")
label = tk.Label(window, text=" Roll to see a random crypto", font=("Arial", 14))
label.pack(pady=20)

def roll_crypto():
    label.config(text="Rolling... (we'll add results soon)")
    button = tk.Button(window, text="TIME TO GAMBA", command=roll_crypto)
    button.pack()

#Define Crypto List with a dictionary
cryptos ={
    1:"Bitcoin",
    2:"Ethereum",
    3:"Ripple",
    4:"Dogecoin",
    5:"Hex",
    6:"Pulsechain" ,
    }

def roll_crypto2():
    roll = random.randint (1, 6)
    chosen = cryptos[roll]
    label.config(text=f"You Rolled for {roll}!\nCrypto: {chosen}")




window.mainloop()
