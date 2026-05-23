# Personal Information Manager

## Project Description

Personal Information Manager is a beginner-friendly Python project developed to practice core programming concepts such as variables, loops, user input, validation, and formatted output.

The program stores personal information, collects user preferences, validates the entered data, and displays everything in a structured and visually clean format.

This project helped me understand how Python programs interact with users and how basic problem-solving is implemented in real applications.

---

# Features

- Stores static personal information
- Accepts user input dynamically
- Prevents empty input using validation
- Uses formatted and aligned output
- Calculates age in months automatically
- Uses string formatting methods
- Includes interactive welcome and goodbye messages
- Handles extra spaces in user input

---

# Technologies Used

- Python 3
- VS Code
- Command Prompt / Terminal

---

# Python Concepts Practiced

- Variables and Data Types
- User Input using `input()`
- While Loops
- Conditional Statements
- Input Validation
- String Methods
- f-Strings
- Formatted Output
- Basic Program Structure

---

# What I Learned

While developing this project, I learned how to:

- Store and manage data using variables
- Take user input dynamically
- Validate incorrect or empty inputs
- Use loops for repeated execution
- Format strings using f-strings
- Improve output readability using spacing and separators
- Use string methods like:
  - `.strip()`
  - `.title()`
  - `.capitalize()`
- Organize a Python project properly

---

# Project Structure

```text
week1-personal-info/
│── personal_info.py
│── README.md
│── test_inputs.txt
└── .gitignore
```

---

# How to Run the Program

## Step 1
Install Python 3 on your system.

## Step 2
Open VS Code or terminal.

## Step 3
Navigate to the project folder.

Example:

```bash
cd week1-personal-info
```

## Step 4
Run the Python file.

```bash
python personal_info.py
```

## Step 5
Enter your favorite food and favorite color when prompted.

---

# Sample Output

```text
╔════════════════════════════════════╗
      PERSONAL INFORMATION MANAGER
╚════════════════════════════════════╝

Welcome to the program!

Enter your favorite food: Pizza
Enter your favorite color: Blue

........................................
      PERSONAL INFORMATION
........................................

Name            : Kavya Sahu
Age             : 19 years
Age in Months   : 228 months
City            : Bhopal
Hobby           : Coding and Reading

----------------------------------------
          USER FAVORITES
----------------------------------------

Favorite Food   : Pizza
Favorite Color  : Blue

========================================
Thank you for using the program!
Have a great day ahead!
========================================
```

---

# Challenges Faced & Solutions

## Challenge 1
Handling empty user input.

### Solution
Used `while` loops to repeatedly ask the user until valid input was entered.

---

## Challenge 2
Making the output look clean and readable.

### Solution
Used separators, spacing, and f-strings for proper formatting.

---

## Challenge 3
Handling unwanted spaces and inconsistent capitalization.

### Solution
Used string methods such as:
- `.strip()`
- `.title()`
- `.capitalize()`

to clean and format the user input.

---

# Testing

The program was tested using:

- Valid inputs
- Empty inputs
- Inputs containing only spaces
- Long text inputs
- Mixed uppercase and lowercase text

All validations and formatting worked correctly during testing.

---

# Future Improvements

Some additional features that can be added in future versions:

- Store data in a file
- Add more user details
- Create a graphical interface
- Add multiple user profiles
- Export information as text

---

# Screenshots

## Program Output

(Add your screenshot here)

---

## Input Validation

(Add your screenshot here)

---

# Author

**Kavya Sahu**  
B.Tech CSE (AI/ML) Student  
Python Beginner Project – Week 1