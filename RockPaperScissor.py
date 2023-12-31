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

import random
names=["Rock","Paper","Scissors"]
images=[rock, paper, scissors]
# User input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_input = random.randint(0,2)

if user_input >= 3 or user_input < 0:
  print("You typed an invalid number!")
else:
  print(f"\nuser choice: {names[user_input]}")
  print(images[user_input])
  print(f"computers choice: {names[computer_input]}")
  print(images[computer_input])

#RULES
if user_input >= 3 or user_input < 0:
  print("You typed an invalid number, you lose!")
elif user_input == 0 and computer_input == 2:
  print("You win!")
elif computer_input == 0 and user_input == 2:
  print("You lose")
elif computer_input > user_input:
  print("You lose")
elif user_input==computer_input:
  print("It's a draw")
elif user_input > computer_input:
  print("You win")
  