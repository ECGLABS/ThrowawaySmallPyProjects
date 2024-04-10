import os
import random
import tkinter as tk
import pygame
import threading

# Initialize pygame mixer
pygame.mixer.init()

# Function to play a random song from a specified folder
def play_random_song(folder):
    print("Playing a random song...")
    # Get a list of files in the specified folder
    files = os.listdir(folder)
    
    # Filter the list to include only files with the desired extension
    song_files = [file for file in files if file.endswith(('.mp3', '.wav'))]
    
    # Check if there are any song files in the folder
    if song_files:
        # Select a random song from the list
        random_song = random.choice(song_files)
        
        # Construct the full path to the selected song
        song_path = os.path.join(folder, random_song)
        print("Selected song:", song_path)
        
        # Load the selected song
        pygame.mixer.music.load(song_path)
        
        # Play the selected song in a separate thread
        threading.Thread(target=pygame.mixer.music.play).start()
        
        # Update currently_playing_label
        currently_playing_label.config(text=f"Currently playing: {random_song}")
    else:
        print("No song files found in the specified folder.")

# Function to be called when the Jazz button is clicked
def button_click_Jazz():
    folder_path = r"Path\To\Your\Jazz\Songs\Folder"  # Change this to the actual path
    play_random_song(folder_path)

# Function to be called when the Rock button is clicked
def button_click_Rock():
    folder_path = r"Path\To\Your\Rock\Songs\Folder"  # Change this to the actual path
    play_random_song(folder_path)

# Function to be called when the Metal button is clicked
def button_click_Metal():
    folder_path = r"Path\To\Your\Metal\Songs\Folder"  # Change this to the actual path
    play_random_song(folder_path)

# Create a new window
window = tk.Tk()

# Set the title of the window
window.title("BackingTracks")

# Set the size of the window
window.geometry("300x250")

# Add buttons to the window
button1 = tk.Button(window, text="Jazz", command=button_click_Jazz)
button1.pack()

button2 = tk.Button(window, text="Rock", command=button_click_Rock)
button2.pack()

button3 = tk.Button(window, text="Metal", command=button_click_Metal)
button3.pack()

# Add label to show currently playing song
currently_playing_label = tk.Label(window, text="Currently playing:")
currently_playing_label.pack(side=tk.BOTTOM, pady=10)

# Run the Tkinter event loop
window.mainloop()
