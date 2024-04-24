"""
rock paper scissors
computer_choice=rock/paper/scissors
user_choice=rock/paper/scissors
"""

import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter rock/paper/scissors: ")
if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("Invalid")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Won")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("you won")
elif user_choice == computer_choice:
    print("game tied")
else:
    print("Computer won", computer_choice)
