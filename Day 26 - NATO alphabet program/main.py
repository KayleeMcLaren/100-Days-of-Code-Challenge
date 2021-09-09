
import pandas

code_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
code_df = pandas.DataFrame(code_dict)

alphabet_dict = {row.letter: row.code for (index, row) in code_df.iterrows()}

user_word = input("Enter a word: ").upper()

code_words = [alphabet_dict[letter] for letter in user_word]

print(code_words)
