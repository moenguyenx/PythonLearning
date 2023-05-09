import pandas

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in nato_df.iterrows():
#     print(row)
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Enter a message: ").upper()
    # Convert a string into a list of letters using list comprehension
    try:
        output = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only word input please!")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
