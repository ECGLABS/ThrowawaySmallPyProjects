import random
import json
import os
import time

# Character state is stored here, this block is called a dictionary
player = {
    "name": "John the Job Seeker",
    "resume_power": 5,
    "networking_skill": 5,
    "cover_letter_charisma": 5,
    "location": "Home",
    "inventory": [],
    "jobs_applied": 0,
    "job_offers": 0
}

# List of places the player can go (you can add more!)
locations = ["Job Board", "Networking Event", "Resume Dungeon", "Interview Tower"]

#Savegame function defined
def save_game():
    """Saves the current player state to a file."""
    with open("savegame.json", "w") as f:
        json.dump(player, f, indent=4)
    print("Game saved!")

def load_game():
    """Loads the game from a file if it exists."""
    if os.path.exists("savegame.json"):
        with open("savegame.json", "r") as f:
            global player
            player = json.load(f)
        print("Game loaded!")
    else:
        print("No saved game found.")

def travel():
    """Lets the player choose a location to travel to."""
    print("\nWhere would you like to go?")
    for i, loc in enumerate(locations):
        print(f"{i + 1}. {loc}")

    choice = input("Enter a number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(locations):
        player["location"] = locations[int(choice) - 1]
        print(f"\nTraveling to {player['location']}...\n")
        encounter_event()
    else:
        print("Invalid choice. Try again.")

def encounter_event():
    """Simulates a random event at the current location."""
    event_roll = random.randint(1, 4)
    if player["location"] == "Job Board":
        if event_roll == 1:
            print("You found a perfect job posting! You apply with confidence.")
            player["jobs_applied"] += 1
        elif event_roll == 2:
            print("You find nothing but unpaid internships.")
        elif event_roll == 3:
            #This event creates an encounter that prompts the user
            while True:
                choice = input("You've encountered an application that wants you to re-enter all your work experience\n on the website.\n Do you still want to apply (yes/no): ").strip().lower()
                if choice == "yes":
                    print("...")
                    time.sleep(3)
                    print("You re-entered everything one by one! You're a masochist! ")
                    player["jobs_applied"] += 1
                    break
                    while True:
                        choice = input(
                            "Would you like to continue your search?(yes/no): ").strip().lower()
                        if choice == "yes":
                            encounter_event()
                            time.sleep(3)
                            print("You re-entered everything one by one! You're a masochist! ")
                            player["jobs_applied"] += 1
                            break



                elif choice == "no":
                    print("You decide your time is more valuable and look at another job")
                    break
                else:
                    print("Please type 'yes' or 'no'.")

        else:
            print("A recruiter ghosted you mid-application.")

    elif player["location"] == "Networking Event":
        if event_roll == 1:
            print("You connected with a tech lead! Networking skill increased.")
            player["networking_skill"] += 1
        else:
            print("You ate all the snacks and avoided everyone. No gains today.")

    elif player["location"] == "Resume Dungeon":
        if event_roll == 1:
            print("You defeated the Grammar Goblin! Resume power increased.")
            player["resume_power"] += 1
        else:
            print("You forgot to save and lost your changes. Ouch.")

    elif player["location"] == "Interview Tower":
        if event_roll == 1:
            print("You nailed the interview! You receive a job offer!")
            player["job_offers"] += 1
        else:
            print("The interviewer asked: 'What's your biggest weakness?' You froze.")



def show_stats():
    """Displays the player's current stats."""
    print("\n=== Player Stats ===")
    for key, value in player.items():
        print(f"{key.capitalize().replace('_', ' ')}: {value}")
    print("====================\n")

def main_menu():
    """Main menu of the game."""
    while True:
        print("What would you like to do?")
        print("1. Travel")
        print("2. Show Stats")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Exit")

        choice = input("Choose an action: ")
        if choice == "1":
            travel()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            save_game()
        elif choice == "4":
            load_game()
        elif choice == "5":
            print("Goodbye, job hunter!")
            break
        else:
            print("Invalid choice. Please select again.\n")

#prompts the user for thier name and stores it as a variable
#name = input("Enter your name Job Seeker:")
#player["name"] = name

#Asks for player to input their name. Then checks if player enter nothing on input and scolds them appropriately
while True:
    name = input("Enter your name job seeker: ").strip()
    if name == "":
        print("A job seeker without a name?! You can't have a resume without a name! Try again!")
    else:
        player["name"] = name
        break

#prints the users name and welcome statement
if __name__ == "__main__":
    print(f"\nWelcome, {player['name']}! \nI've seen many like you in my time.\n Will you break the unemployment curse \n or be another lost to the couch...\n")




    main_menu()
