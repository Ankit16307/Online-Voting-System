import os
import time

USERS_FILE = "users.txt"
VOTES_FILE = "votes.txt"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Track activity for fraud detection
login_attempts = {}
vote_timestamps = []

# Default candidates
candidates = {
    "BJP": 0,
    "INC": 0,
    "AAP": 0,
    "CPI": 0,
    "JMM": 0,
    "BSP": 0,
    "DMK": 0,
    "TMC": 0,
    "RJD": 0,
    "SP": 0,
    "JDS": 0,
    "SHS": 0
}

# ---------------- FILE HANDLING ----------------

def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                username, password, voted = line.strip().split(",")
                users[username] = {
                    "password": password,
                    "voted": voted == "True"
                }
    return users

def save_users(users):
    with open(USERS_FILE, "w") as f:
        for username, data in users.items():
            f.write(f"{username},{data['password']},{data['voted']}\n")

def load_votes():
    if os.path.exists(VOTES_FILE):
        with open(VOTES_FILE, "r") as f:
            for line in f:
                name, count = line.strip().split(",")
                if name in candidates:
                    candidates[name] = int(count)

def save_votes():
    with open(VOTES_FILE, "w") as f:
        for name, count in candidates.items():
            f.write(f"{name},{count}\n")

# Initialize data
users = load_users()
load_votes()

# ---------------- FRAUD DETECTION ----------------

def detect_login_fraud(username):
    current_time = time.time()
    if username not in login_attempts:
        login_attempts[username] = []

    login_attempts[username].append(current_time)

    # Keep only last 5 attempts
    login_attempts[username] = login_attempts[username][-5:]

    if len(login_attempts[username]) >= 5 and (current_time - login_attempts[username][0] < 10):
        print("⚠️ Suspicious activity detected: Too many login attempts!\n")

def detect_vote_spike():
    current_time = time.time()
    vote_timestamps.append(current_time)

    # Keep last 10 votes
    recent = vote_timestamps[-10:]

    if len(recent) >= 5 and (recent[-1] - recent[0] < 5):
        print("⚠️ Suspicious voting spike detected!\n")

# ---------------- USER FUNCTIONS ----------------

def register():
    global users
    username = input("Enter username: ")
    if username in users:
        print("User already exists!")
        return

    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match!\n")
        return

    users[username] = {"password": password, "voted": False}
    save_users(users)
    print("Registration successful!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    detect_login_fraud(username)  # ✅ fraud check

    if username in users and users[username]["password"] == password:
        print("Login successful!\n")
        return username
    else:
        print("Invalid credentials!\n")
        return None

def vote(username):
    global users
    if users[username]["voted"]:
        print("You have already voted!\n")
        return

    print("\nCandidates:")
    for i, candidate in enumerate(candidates.keys(), start=1):
        print(f"{i}. {candidate}")

    try:
        choice = int(input("Enter candidate number: "))
        candidate_list = list(candidates.keys())

        if 1 <= choice <= len(candidate_list):
            selected = candidate_list[choice - 1]
            candidates[selected] += 1
            users[username]["voted"] = True

            detect_vote_spike()  # ✅ fraud check

            save_votes()
            save_users(users)

            print(f"Vote casted for {selected}!\n")
        else:
            print("Invalid choice!\n")
    except:
        print("Invalid input!\n")

def show_results():
    print("\nVoting Results:")
    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)

    for candidate, votes in sorted_candidates:
        print(f"{candidate}: {votes} votes")

# ---------------- ADMIN ----------------

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Admin login successful!\n")
        admin_panel()
    else:
        print("Invalid admin credentials!\n")

def reset_user_vote():
    username = input("Enter username to reset vote: ")

    if username in users:
        users[username]["voted"] = False
        save_users(users)
        print("User vote reset successfully!\n")
    else:
        print("User not found!\n")

def add_candidate():
    name = input("Enter new candidate name: ")
    if name in candidates:
        print("Candidate already exists!\n")
    else:
        candidates[name] = 0
        save_votes()
        print("Candidate added successfully!\n")

def remove_candidate():
    name = input("Enter candidate name to remove: ")
    if name in candidates:
        del candidates[name]
        save_votes()
        print("Candidate removed successfully!\n")
    else:
        print("Candidate not found!\n")

def reset_all_votes():
    for key in candidates:
        candidates[key] = 0
    save_votes()

    for user in users:
        users[user]["voted"] = False
    save_users(users)

    print("All votes reset successfully!\n")

def admin_panel():
    while True:
        print("\n===== Admin Panel =====")
        print("1. Reset User Vote")
        print("2. Add Candidate")
        print("3. Remove Candidate")
        print("4. Reset All Votes")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            reset_user_vote()
        elif choice == "2":
            add_candidate()
        elif choice == "3":
            remove_candidate()
        elif choice == "4":
            reset_all_votes()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

# ---------------- MAIN ----------------

def main():
    while True:
        print("\n===== Online Voting System =====")
        print("1. Register")
        print("2. Login")
        print("3. Show Results")
        print("4. Admin Login")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                vote(user)

        elif choice == "3":
            show_results()

        elif choice == "4":
            admin_login()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
