
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

game_image_variables = [rock, paper, scissors]

# user choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
user_choice_as_int = int(user_choice)
print(f"User chose: {game_image_variables[user_choice_as_int]}\n") # use the integer value of 'user_choice_as_int' as the index of the list 'game_image_varaibles' to print image

# computer choice
computer_choice = random.randint(0, 2)
print(f"Computer chose: {game_image_variables[computer_choice]}\n") 

if user_choice_as_int == computer_choice:
    print("It's a draw.")

elif user_choice_as_int == 0:
    if computer_choice == 2:
        print("You Win!")
    else:
        print("You Lose.")

elif user_choice_as_int == 1:
    if computer_choice == 0:
        print("You Win!")
    else:
        print("You Lose.")

elif user_choice_as_int == 2:
    if computer_choice == 1:
        print("You Win!")
    else:
        print("You Lose.")

else:
    print("You typed an invalid number")
