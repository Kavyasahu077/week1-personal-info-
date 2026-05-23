# ==========================================
# Name: Kavya Sahu
# Project: Personal Information Manager
# Description:
# This program stores and displays personal
# information using variables, input/output,
# string formatting, and validation.
# ==========================================

# Welcome message
print("=" * 50)
print("        PERSONAL INFORMATION MANAGER")
print("=" * 50)
print()

# ------------------------------------------
# Static Information
# ------------------------------------------

# Store personal details in variables
name = "Kavya Sahu"          # String variable
age = 19                     # Integer variable
city = "Bhopal"              # String variable
hobby = "Coding and Reading" # String variable

# ------------------------------------------
# User Input Section
# ------------------------------------------

print("Please enter the following details:")
print("-" * 40)

# Get favorite food from user
favorite_food = input("What is your favorite food? ").strip()

# Validate empty input
while favorite_food == "":
    print("Favorite food cannot be empty!")
    favorite_food = input("Please enter your favorite food: ").strip()

# Get favorite color from user
favorite_color = input("What is your favorite color? ").strip()

# Validate empty input
while favorite_color == "":
    print("Favorite color cannot be empty!")
    favorite_color = input("Please enter your favorite color: ").strip()

# ------------------------------------------
# Additional Calculation
# ------------------------------------------

# Calculate age in months
age_in_months = age * 12

# ------------------------------------------
# Display Information
# ------------------------------------------

print()
print("=" * 50)
print("             YOUR INFORMATION")
print("=" * 50)

# Use string methods for formatting
print(f"Name            : {name.title()}")
print(f"Age             : {age} years")
print(f"Age in Months   : {age_in_months} months")
print(f"City            : {city.title()}")
print(f"Hobby           : {hobby.title()}")

print("-" * 50)

print(f"Favorite Food   : {favorite_food.title()}")
print(f"Favorite Color  : {favorite_color.title()}")

print("=" * 50)

# Goodbye message
print("Thank you for using the program!")
print("Have a great day!")
print("=" * 50)