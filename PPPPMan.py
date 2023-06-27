import tkinter as tk
from tkinter import font

def display_text():
    # Create a new window
    window = tk.Toplevel(root)
    
    # Set the window title
    window.title("Text Display")
    
    # Create a label with large font
    font_style = font.Font(size=30, weight="bold")
    label = tk.Label(window, text="I am the pee pee poo poo man", font=font_style)
    label.pack(padx=50, pady=50)

# Create the main window
root = tk.Tk()
root.title("Pee Pee Poo Poo App")

# Create a button to display the text
button = tk.Button(root, text="Display Text", command=display_text)
button.pack(padx=50, pady=50)

# Run the main event loop
root.mainloop()