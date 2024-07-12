
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)
def get_word():
    word = input("Enter a word: ").upper()
    try:
        output_list = [dict[letter] for letter in word]
    except KeyError:
        print("Alphabet answers only, try again")
        get_word()
    else:
        print(output_list)
get_word()
