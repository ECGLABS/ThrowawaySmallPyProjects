import random
import time
import sys

def catch_the_fish():
    fish_positions = ["🐟       ", " 🐟      ", "  🐟     ", "   🐟    ", "    🐟   ", "     🐟  ", "      🐟 "]
    print("🎣 Welcome to 'Catch the Fish!' 🎣")
    print("Press ENTER when the fish is in the center!")
    print("Get ready...")
    time.sleep(2)

    try:
        while True:
            for i in range(random.randint(15, 25)):
                pos = random.choice(fish_positions)
                sys.stdout.write("\r" + pos)
                sys.stdout.flush()
                time.sleep(0.1)
            start = time.time()
            input("\n🎯 NOW! Press ENTER!")
            reaction_time = time.time() - start
            if 2.5 < reaction_time < 3.5:
                print("🏆 Great catch! You got the fish!")
            else:
                print(f"🐟 Oh no! Your reaction time was {reaction_time:.2f} seconds. Try again!\n")
            play_again = input("Play again? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing! Goodbye!")
                break
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")

if __name__ == "__main__":
    catch_the_fish()
