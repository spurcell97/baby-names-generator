import random, string
from string import ascii_lowercase


def generator ():
    letter1 = random.choice(ascii_lowercase)
    letter2 = random.choice(ascii_lowercase)
    letter3 = random.choice(ascii_lowercase)
    letter4 = random.choice(ascii_lowercase)
    letter5 = random.choice(ascii_lowercase)
    name = letter1+letter2+letter3+letter4+letter5
    return(name)

print(generator())

#lets now ask user for some input

letter_input_1 = raw_input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')  # type: object
letter_input_3 = raw_input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_4 = raw_input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_5 = raw_input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase

if letter_input_1 == "v":
    letter1 = random.choice(vowels)
elif letter_input_1 == "c":
    letter1 = random.choice(consonants)
elif letter_input_1 == "l":
    letter1 = random.choice(letter)
else:
    letter1 = letter_input_1



