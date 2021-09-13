
import pandas

code_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
code_df = pandas.DataFrame(code_dict)

alphabet_dict = {row.letter: row.code for (index, row) in code_df.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        code_words = [alphabet_dict[letter] for letter in user_word]

    except KeyError:
        print("\nSorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(code_words)


generate_phonetic()
