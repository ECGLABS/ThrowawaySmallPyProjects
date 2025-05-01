import tkinter as tk

#tkinter window generation code
window = tk.Tk()
window.title("Crypto Roller")
window.geometry("400x400")
label = tk.Label(window, text=" Roll to see a random crypto", font=("Arial", 14))
label.pack(pady=20)

def roll_crypto():
    label.config(text="Rolling... (we'll add results soon)")
    button = tk.Button(window, text="COME TIME TO GAMBA", command=roll_crypto)
    button.pack()


window.mainloop()
