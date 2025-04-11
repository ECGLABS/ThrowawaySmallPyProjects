import random
from datetime import datetime

fortunes = [
    "You will find what you seek in the most unexpected place.",
    "Great success is coming your way, just keep going.",
    "An old friend will bring new opportunities.",
    "Your talents will be recognized and rewarded.",
    "The path you're on will lead to greatness.",
    "Don't forget to water your dreams.",
    "You will master something that once seemed impossible.",
    "Change is coming—embrace it."
]

def open_cookie():
    fortune = random.choice(fortunes)
    print("\n🥠 Your Fortune Cookie says:")
    print(f"➡️  {fortune}")
    return fortune

def save_fortune(fortune):
    with open("fortune_journal.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {fortune}\n")
    print("📝 Fortune saved to journal.")

if __name__ == "__main__":
    f = open_cookie()
    save = input("\nDo you want to save this fortune to your journal? (y/n): ").strip().lower()
    if save == "y":
        save_fortune(f)
    else:
        print("🗑️  Fortune discarded. On to the next adventure!")
