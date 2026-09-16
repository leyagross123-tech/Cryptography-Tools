from collections import Counter
import math

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
standard_freqs = [8.04, 1.53, 3.1, 3.97, 12.5, 2.33, 1.95, 5.44,7.29,
                  0.16, 0.66, 4.13, 2.54, 7.1, 7.59, 2.02, 0.11, 6.13,
                  6.55, 9.25, 2.71, 1.0, 1.88, 0.2, 1.72, 0.1]

def validate(inpt, expected_type):
    # validates whether a given input is as expected
    if type(inpt) != expected_type:
        print("Your input was unexpected. It had the type " +
              str(type(inpt)) + " rather than " + str(expected_type) + '.')
        return False
    return True

def get_text():
    # function to accept multi-line inputs
    print("Paste text. Press Ctrl+D (Linux/Mac) or Ctrl+Z " +
          "then Enter (Windows) when finished.")
    text = ""
    try:
        while True:
            text += input() + "\n"
    except EOFError:
        pass
    return text

def clean(text, space=''):
    # Convert text to uppercase, optionally preserve spaces, and
    # remove all non-alphabetic characters.
    if not validate(text, str):
        return ''
    
    text = text.upper().replace('\n', space).replace(' ', space)
    text = ''.join(char for char in text if char.isalpha() or char == space)
    return text

def unique(string):
    # Return a list of the unique words found in a text string
    if not validate(string, str):
        return []
    return list(set(clean(string, ' ').split()))

def letter_freqs(text, spaces=False):
    # Cleans text, optionally allowing spaces, then counts the number of occurences
    # for each letter in the alphabet, appending them in order.
    ##----!TODO: "letters" should be a dictionary but I'm not confident with that!----##
    text = clean(text, space='' if not spaces else ' ')
    if not validate(text, str) or text == '':
        return []
    letters = []
    letters = [round(text.count(char)/len(text) * 100, 2) for char in ALPHABET]
    if spaces:
        letters.append(text.count(' ')/len(text) * 100)
        
    return letters
def tetragram_freqs(text):
    # Writes tetragram frequencies to a file named by the user.
    # for tetragram frequencies in the Brown corpus, see text file in my Python folder.
    text = clean(text)
    
    if not validate(text, str) or len(text) < 4:
        return
    
    tetragrams = []
    pointer = 0
    while pointer != len(text)-3:
    # i.e. whilst pointer is not pointing to the fourth-last letter
        tetragrams.append(text[pointer:pointer+4])
        pointer += 1
    frequencies = Counter(tetragrams).most_common()
    file_name = input('What to name the file? ') + '.csv'
    
    with open(file_name,'w') as file:
        for item, count in frequencies:
            count = round(count/len(tetragrams) * 100, 10)
            if count < 0.0000001:
                continue
            file.write(f"{item},{count}\n")
        print(f'Tetragram frequencies successfully written to {file_name}')

def X_squared(measured, expected):
    # Finds the X-squared characteristic for data.
    # Hasn't worked for text as text data files contained whitespace and readability formatting.
    statistic = 0
    for i in range(len(measured)):
        statistic = statistic + ((measured[i] - expected[i])**2) / expected[i]
    return statistic

def X_squared_text(text):
    text = clean(text)
    observed = []
    expected = []
    for char in ALPHABET:
        observed.append(text.count(char))
    for frequency in standard_freqs:
        expected.append(len(text) * frequency / 100)
    return X_squared(observed, expected)

def inner_product(vector1, vector2):
    # finds the dot product of two vectors
    # used in cosine angle function
    dot_product = int()
    
    if len(vector1) != len(vector2):
        print('ERROR!' * 59)
        return 'Error #♾️: the length of the two vectors do not match'
    for i in range(len(vector1)):
        dot_product = dot_product + (vector1[i] * vector2[i])
    return dot_product

def find_cosine_angle(vector1, vector2=standard_freqs):
    # the smaller the cosine similarity, the closer the vectors match
    # here is the mathematical formula for the cosine angle of vectors:
    # U⋅V/√(U⋅U)(V⋅V)
    try:
        return inner_product(vector1, vector2)/math.sqrt(inner_product(vector1, vector1)* inner_product(vector2, vector2))
    except TypeError:
        print('\n\nPlease stay calm, I ran into an error. Here\'s the error code:', inner_product(vector1, vector2))
        
def IOC(text, blocksize = 1):
    # The formula for the IoC of a given text is IoC = 26*∑(ni(ni-1))/N(N-1).
    # The average IoC for English plaintext is 1.73, and random text would be about 1.0
    # The IoC for the Brown Corpus is 1.7096108454908279.
    IoC = 0
    blocks = []
    counter = 0
    block = ''
    
    for char in text:
        block = block + char
        counter = counter + 1
        if counter == blocksize:
            blocks.append(block)
            block = ''
            counter = 0
    freqs = Counter(blocks)
    
    for number in freqs.values():
        IoC += (number * (number - 1)) / (len(text) * (len(text) - 1))
    print(freqs)
    return (IoC * 26)
def shift_by(amount):
    # shifts the alphabet by a given amount
    # if amount is 2, then the shifted alphabet starts with c.
    amount %= len(ALPHABET)
    new_alph = ALPHABET[amount:]
    new_alph = new_alph + ALPHABET[0:amount]
    return new_alph

def caesar(text, key, encrypt=False, alph=ALPHABET):
    # implements the caesar shift on a given ciphertext. Assumes cleaned text.
    # is used in more complex functions, such as vignere and beaufort cipher decryption.
    if not encrypt:
        key = -key

    key %= len(alph)

    result = ''

    for char in text:
        pos = alph.index(char)
        result += alph[(pos + key) % len(alph)]

    return result

def parse(text):
    # an imperfect function that tries to parse decrypted text.
    # without NLP I don't see how it can be perfect. Still, it's pretty awful.
    dictionary = open('ranked_dict.txt').read().splitlines()
    pointer = 0
    proper_split = []
    while pointer < len(text):
        matches = []
        for word in dictionary:
            if text.startswith(word, pointer):
                matches.append(word)
        if not matches:
            proper_split.append(text[pointer])
            pointer += 1
            continue
        best = max(matches, key=len)
        proper_split.append(best)
        pointer += len(best)
    return (' '.join(proper_split).lower())
