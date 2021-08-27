#Please run this code on https://replit.com/~ in order to use the clear() function

import random
from game_data import data
from art import logo, vs
from replit import clear


def format_account(account):
  """Format the account into printable format"""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_description}, from {account_country}"


def check_guess(user_guess, account_one_followers, account_two_followers):
  """Take the user guess and follower counts and return if they got it right"""
  if account_one_followers > account_two_followers:
      return user_guess == 'a'
  else:
    return user_guess == 'b'

"""Game starts here"""
print(logo)
score = 0
game_continue = True

"""Generate the second account outside the while loop so that the second account shifts up into the place of the first account after each round of the game"""
account_two = random.choice(data)

while game_continue:

  account_one = account_two
  account_two = random.choice(data)

  while account_one == account_two: # checks if the same account was randomly generated for both account_one and account_two and if so, regenerates another account
    account_two = random.choice(data)

  print(f"Compare A: {format_account(account_one)}")
  print(vs)
  print(f"Compare B: {format_account(account_two)}")

  user_guess = input("\nWho has the most Instagram followers. Type 'A' or 'B': ").lower()

  account_one_followers = account_one['follower_count'] # gets the number of followers for each account
  account_two_followers = account_two['follower_count']
  is_correct = check_guess(user_guess, account_one_followers, account_two_followers) # calls the check_guess function to compare the number of followers

  clear() # clears the screen after every turn

  """Check if user guess is correct"""
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_continue = False
    
