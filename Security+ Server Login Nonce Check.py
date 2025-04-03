import hashlib
import uuid
from datetime import datetime

# Simple dynamic user database (for demo purposes)
user_db = {}

# Nonce tracking per user: {username: (nonce, timestamp)}
user_nonces = {}

def generate_nonce():
    return uuid.uuid4().hex

def hash_with_nonce(password, nonce):
    return hashlib.sha256((password + nonce).encode()).hexdigest()

def verify_login(username, client_hash, nonce):
    # Check for replay
    if username in user_nonces and user_nonces[username][0] == nonce:
        print("❌ Replay detected! This nonce was already used for this user.\n")
        return False

    expected_hash = hash_with_nonce(user_db[username], nonce)
    if expected_hash == client_hash:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_nonces[username] = (nonce, timestamp)
        print(f"✅ Login successful at {timestamp}!\n")
        return True
    else:
        print("❌ Invalid credentials.\n")
        return False

while True:
    print("=== Secure Multi-User Login Simulator ===")
    username = input("Enter username (or type 'exit' to quit): ").strip()
    if username.lower() == 'exit':
        break

    # Auto-generate password for demo users if not found
    if username not in user_db:
        password = f"{username}_pass"
        user_db[username] = password
        print(f"[Info] Created new user '{username}' with password '{password}'")

    # Handle existing users with nonce history
    reuse = False
    if username in user_nonces:
        last_nonce, timestamp = user_nonces[username]
        print(f"[Server] Previous nonce issued at {timestamp}")
        choice = input("Reuse the last nonce? (y = keep / n = clear): ").strip().lower()
        if choice == 'y':
            nonce = last_nonce
            reuse = True
        else:
            nonce = generate_nonce()
    else:
        nonce = generate_nonce()

    print(f"[Server] Your nonce: {nonce}")

    # Simulate hashing on the client side
    password = user_db[username]
    hashed_response = hash_with_nonce(password, nonce)
    print(f"[Client] Sending hashed credentials...")

    # Verify on the server side
    verify_login(username, hashed_response, nonce)

    again = input("Try another login? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 Exiting simulator.")
        break

    print("\n" + "="*50 + "\n")
