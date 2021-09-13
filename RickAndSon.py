#This program takes in information from a user
import sys

def user_data():
    name = input("Please enter a name:\n")
    age = input("Please enter an age:\n")
    gender = input("Please enter a gender:\n")
    hobby = input("Please enter a hobby:\n")

answer = input("Enter a 1 to create an account, enter anything else to exit:\n")
if answer == '1':
    user_data()
else:
    sys.exit()

