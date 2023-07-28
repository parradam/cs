# A function that returns the first nonduplicated character in a string

def find_nonduplicated_letter(str):    
    letter_count = {}

    # Build the array of letters and their counts
    for letter in str:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
    # Loop through string and find first nonduplicated letter
    for letter in str:
        if letter_count[letter] == 1:
            return letter
    
    return None

str = 'minimum'

print(find_nonduplicated_letter(str))