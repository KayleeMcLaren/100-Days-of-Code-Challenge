
random_word = random.choice(word_list)
random_word_length = len(random_word)

end_of_game = False
user_lives = 6

# create blanks
blank_spaces_list = []
for letter in random_word:
    blank_spaces_list += "-"

# game start
print(logo)
while not end_of_game:
    user_guess = input("Guess a letter: \n").lower()
    if user_guess in blank_spaces_list:
        print(f"You've already guessed the letter '{user_guess}'.")

    # check user guess is correct
    for index in range(random_word_length):
        letter_in_random_word = random_word[index]
        if letter_in_random_word == user_guess:
            blank_spaces_list[index] = letter_in_random_word

    # check if user guesses incorrectly
    if user_guess not in random_word:
        print(f"The letter '{user_guess}' is not in the word. You lose a life.")
        user_lives -= 1
        if user_lives == 0:
            end_of_game = True
            print(f"\nYou lose! The word was {random_word}")

    # join all the elements in blank_spaces_list and display as a String
    print(f"{' '.join(blank_spaces_list)}")

    # check if all blank spaces are filled
    if "-" not in blank_spaces_list and user_lives > 0:
        end_of_game = True
        print("\nYou won!")

    # print hangman image
    print(stages[user_lives])
    
