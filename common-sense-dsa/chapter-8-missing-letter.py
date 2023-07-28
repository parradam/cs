# A function that returns the missing letter of the alphabet from a string

def find_missing_letter(str):    
    array_dict = {}

    for letter in str:
        if not array_dict.get(letter, False):
            array_dict[letter] = True
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:
        if not array_dict.get(letter, False):
            return letter
    
    return None

str = 'the quick brown box jumps over a lazy dog'

print(find_missing_letter(str))