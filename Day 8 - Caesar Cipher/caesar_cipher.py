
from caesar_art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# caesar function
def caesar_cipher(user_text, shift_count, direction_choice):
    cipher_text = ""

    if direction_choice == "decode":
        shift_count *= -1  # to reverse the direction
    for char in user_text:
        if char in alphabet:  # only encrypts letters
            index_in_alphabet = alphabet.index(char)
            shifted_index = index_in_alphabet + shift_count
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += char

    print(f"The {direction_choice}d text is: {cipher_text}\n")


# Program start
print(logo)

run_again = True
while run_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # ensures that the 'shift' number fits within the alphabet list, no matter how large it is

    caesar_cipher(user_text=text, shift_count=shift, direction_choice=direction)

    # check if the user wants to run the program again
    restart = input("Type 'yes' if you want to start again or type 'no' to end the program.\n")
    if restart == "no":
        run_again = False
        print("\nProgram ended.")
