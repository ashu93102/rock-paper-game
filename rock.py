#rock paper scissors game
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to rock paper scissors")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("you choose: ")

#user condition
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    ("Invalid Choice")

comp_choice = random.randint(0, 2)

print("Computer choose: ")

#computer section
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)
else:
    ("Invalid Choice")

# checking wo wins
if user_choice == 0 and comp_choice == 1:
    print("You Loose")
if user_choice == 1 and comp_choice == 1:
    print("Draw")
if user_choice == 2 and comp_choice == 1:
    print("You win")
if user_choice == 0 and comp_choice == 2:
    print("You Win")
if user_choice == 1 and comp_choice == 2:
    print("You Loose")
if user_choice == 2 and comp_choice == 2:
    print("Draw")
if user_choice == 0 and comp_choice == 0:
    print("Draw")
if user_choice == 1 and comp_choice == 0:
    print("You Win")
if user_choice == 2 and comp_choice == 0:
    print("You Loose")