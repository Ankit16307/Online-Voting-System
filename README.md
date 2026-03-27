---

#  Online Voting System (CLI)

A simple **Command-Line Based Online Voting System** built using Python.
This project allows users to register, login, and vote securely, while providing an admin panel to manage candidates and votes.

---

##  Features

* User Registration & Login
* Secure Voting (One vote per user)
* Admin Panel for management
* Add / Remove Candidates
* Reset Individual or All Votes
* Results displayed in descending order
* Data persistence using `.txt` files
* Menu-driven CLI interface

---

##  Technologies Used

* Python
* File Handling (.txt files)
* CLI (Command Line Interface)

---

##  File Structure

```
📁 Online-Voting-System
 ├── main.py
 ├── users.txt
 ├── votes.txt
 └── README.md
```

---

##  How to Run

1. Make sure Python is installed
2. Clone the repository:

```
git clone https://github.com/your-username/online-voting-system.git
```

3. Navigate to the folder:

```
cd online-voting-system
```

4. Run the program:

```
python main.py
```

---

##  User Functionalities

* Register a new account
* Login with credentials
* Cast vote (only once)
* View voting results

---

##  Admin Functionalities

* Login using admin credentials
* Add new candidates
* Remove candidates
* Reset individual user vote
* Reset all votes

> Default Admin Credentials:

```
Username: admin
Password: admin123
```

---

##  Data Storage

* **users.txt** → stores user credentials and voting status
* **votes.txt** → stores candidate names and vote counts

---

##  System Design

* Modular programming approach
* File-based data persistence
* Separation of:

  * User Interface (CLI)
  * Logic (Functions)
  * Storage (Text files)

---

##  Limitations

* No encryption for passwords
* CLI-based interface (no GUI)
* Not suitable for large-scale deployment
* No database integration

---

##  Future Enhancements

* Add GUI (Tkinter / Web App)
* Use database (MySQL / MongoDB)
* Implement password hashing
* Add user session management
* Deploy as a web-based application

---

##  Sample Output

```
===== Online Voting System =====
1. Register
2. Login
3. Show Results
4. Admin Login
5. Exit
```

---

##  References

* Python Documentation
* Online tutorials and learning resources

---


