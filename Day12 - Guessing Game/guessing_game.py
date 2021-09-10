

import random
from guessing_game_art import logo

check_continue = True
attempts = 0
number = random.randrange(1, 100)  # chooses an random number between 1 and 100


def play_guessing_game():
    """Sets the number of attempts the user has based on the difficulty the user selects and then calls the check_guess
        function, while the check_continue variable is True"""
    global attempts
    global check_continue

    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if game_mode == 'easy':
        attempts = 10
    else:
        attempts = 5

    while check_continue:
        check_guess()


def check_guess():
    """If the user has run out of attempts, the game will end and the user loses. If not, it shows the user how many 
        attempts they have and asks them to make a guess. Then checks that guess against the number and determines if 
        the user's guess was high lower, or equal to the number"""
    global attempts
    global check_continue
    global number

    while check_continue:
        if attempts == 0:  # if the player has used up all their attempts, the game ends and they lose
            print(f"\nYou lose! The number was {number}")
            print("Game Over")
            check_continue = False

        else:
            print(f"\nYou have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
            attempts -= 1

            if user_guess > number:
                print("Too high")
            elif user_guess < number:
                print("Too low")
            else:
                print(f"You win! The number was {number}")  # if the player guesses correctly, they win and the game ends
                check_continue = False


"""Game starts here"""
print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")
play_guessing_game()
