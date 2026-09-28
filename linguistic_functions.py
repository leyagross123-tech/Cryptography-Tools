'''Functions in this library:
get_text,clean,validate

letter_freqs, tetragram_freqs_file, tetragram_freqs,
X_squared, X_squared_text, inner_product, IOC,
find_cosine_angle, get_fittest

is_mono, unique, gen, shift_by, parse,
split_blocks, get_slice
'''
from collections import Counter
import math, random, time

ENGLISH_TET_FREQS = {}
ENGLISH_TET_VECTOR = []
with open("english_tet_freqs.csv", "r") as file:
    for line in file:
        tetragram, freq = line.strip().split(',')
        ENGLISH_TET_FREQS[tetragram] = float(freq)
        ENGLISH_TET_VECTOR.append(float(freq))
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
standard_freqs = [8.04, 1.53, 3.1, 3.97, 12.5, 2.33, 1.95, 5.44,7.29,
                  0.16, 0.66, 4.13, 2.54, 7.1, 7.59, 2.02, 0.11, 6.13,
                  6.55, 9.25, 2.71, 1.0, 1.88, 0.2, 1.72, 0.1]

####################################################################################
#----------------FUNCTIONS FOR INPUT PREP------------------------------------------#
####################################################################################
def get_text():
    # function to accept multi-line inputs
    print("Paste text. Press Ctrl+D then Enter when finished.")
    text = ""
    try:
        while True:
            text += input() + "\n"
    except EOFError:
        pass
    return clean(text)

def clean(text, space=''):
    # Convert text to uppercase, optionally preserve spaces, and
    # remove all non-alphabetic characters.
    if not validate(text, str):
        return ''
    
    text = text.upper().replace('\n', space).replace(' ', space)
    text = ''.join(char for char in text if char.isalpha() or char == space)
    return text

def validate(inpt, expected_type):
    # validates whether a given input is as expected
    if type(inpt) != expected_type:
        print("Your input was unexpected. It had the type " +
              str(type(inpt)) + " rather than " + str(expected_type) + '.')
        return False
    return True

####################################################################################
#----------------FUNCTIONS FOR GETTING DATA----------------------------------------#
####################################################################################
def letter_freqs(text, spaces=False):
    # Cleans text, optionally allowing spaces, then counts the number of occurences
    # for each letter in the alphabet, appending them in order.
    text = clean(text, space='' if not spaces else ' ')
    if not validate(text, str) or text == '':
        return []
    letters = [round(text.count(char)/len(text) * 100, 2) for char in ALPHABET]
    if spaces:
        letters.append(text.count(' ')/len(text) * 100)
    return letters

def tetragram_freqs_file(text):
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

def tetragram_freqs(text):
    # Writes tetragram frequencies to a file named by the user.
    # for tetragram frequencies in the Brown corpus, see text file in my Python folder.
    text = clean(text)
    results = []
    if not validate(text, str) or len(text) < 4:
        print('EARLY RETURN')
        return
    tetragrams = []
    pointer = 0
    while pointer != len(text)-3:
    # i.e. whilst pointer is not pointing to the fourth-last letter
        tetragrams.append(text[pointer:pointer+4])
        pointer += 1
    frequencies = Counter(tetragrams).most_common()
    for item, count in frequencies:
        count = round(count/len(tetragrams) * 100, 10)
        if count < 0.0000001:
            continue
        results.append([item, count])
    return results
            
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
    return -1 * X_squared(observed, expected)

def inner_product(vector1, vector2):
    # finds the dot product of two vectors
    # used in cosine angle function
    dot_product = int()
    if len(vector1) != len(vector2):
        print(vector1, vector2)
        print('Error #♾️: the length of the two vectors do not match')
        time.sleep(5)
        return 0
    for i in range(len(vector1)):
        try:
            dot_product = dot_product + (vector1[i] * vector2[i])
        except TypeError:
            print('Error #❣️: two diffy types')
            time.sleep(5)
            return 0
    return dot_product

def find_cosine_angle(vector1, vector2=standard_freqs):
    # the smaller the cosine similarity, the closer the vectors match
    # here is the mathematical formula for the cosine angle of vectors:
    # U⋅V/√(U⋅U)(V⋅V)
    if type(vector1) == str:
        vector1 = letter_freqs(vector1)
    try:
        return inner_product(vector1, vector2)/math.sqrt(inner_product(vector1, vector1)* inner_product(vector2, vector2))
    except ZeroDivisionError:
        print('\n\nHello, Houston? Cosine_angle here. I am unable to complete the task.\nHELLOO??')
        time.sleep(5)
        return inner_product(vector1, vector2)
    

ENGLISH_TET_MAGNITUDE = math.sqrt(
    inner_product(ENGLISH_TET_VECTOR, ENGLISH_TET_VECTOR)
)

ENGLISH_TET_FREQS[tetragram] = float(freq)

def tetra_fitness(text):
    if text == None:
        return float('-inf')

    if len(text) < 4:
        return float('-inf')

    score = 0

    for tet, freq in tetragram_freqs(text):
        if tet in ENGLISH_TET_FREQS:
            score += freq * math.log(ENGLISH_TET_FREQS[tet])
        else:
            score += freq * math.log(0.00001)

    return score

def IOC(text, blocksize = 1):
    # The formula for the IoC of a given text is IoC = 26*∑(ni(ni-1))/N(N-1).
    # The average IoC for English plaintext is 1.73, and random text would be about 1.0
    # The IoC for the Brown Corpus is 1.7096108454908279.
    if len(text) < 2:
        return 0 #IoC is undefined for too short lengths
    
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
    return (IoC * 26)

def get_fittest(results, method=tetra_fitness, number=1):
    scored = []
    for result in results:
        scored.append((method(result), result))
    scored.sort(reverse=True)
    return scored

####################################################################################
#----------------FUNCTIONS FOR INPUT MANIPULATION----------------------------------#
####################################################################################
def is_mono(text):
  # determines whether ciphertext is monoalphabetic
    ioc_text = IOC(text)
    #standard IOC = ~1.7
    fitness = find_cosine_angle(text)
    if (ioc_text < 2 and ioc_text > 1.3) and (fitness < 0.8):
        # adjust these value to be stricter or less strict. I set them at a guess
        return True
    return False

def unique(string=''):
    # Return a list of the unique words found in a text string
    if not validate(string, str):
        return []
    return list(set(string.split()))

def gen(word_list='', mode='L', alph=ALPHABET):
    # generates an alphabet key from a keyword
    # choose mode L to generate a key appending the alphabet from the last letter of the keyword
    key_list = []
    if word_list == '': #dictionary attack
        with open('ranked_dict.txt','r') as file:
            word_list = file.read().split('\n')
    if type(word_list)==str:
        word_list = [word_list]
    for key in word_list:
        if key == 'PRISM':
            print('It\'s in the dict')
        temp = ''
        for letter in key:
            if letter not in temp:
                temp = temp + letter
            key = temp
        if mode != 'L': #L = last letter mode
            for char in ALPHABET:
                if char not in key:
                    key = key + char
        else:
            temp = key + alph[alph.index(key[-1])+1:] + alph[:alph.index(key[-1])]
            key = ''
            for char in temp:
                if char not in key:
                    key = key + char
        key_list.append(key)
    return key_list

def shift_by(amount=0):
    # shifts the alphabet by a given amount
    # if amount is 2, then the shifted alphabet starts with c.
    amount %= len(ALPHABET)
    new_alph = ALPHABET[amount:]
    new_alph = new_alph + ALPHABET[0:amount]
    return new_alph

def parse(text=''):
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

def split_blocks(text='', number=1):
    # Splits text into n blocks, adding every nth letter to block
    blocks = []
    block = ''
    starter = 0
    while starter != number:
        for char in range(starter, len(text), number):
            block = block + text[char]
        blocks.append(block)
        block = ''
        starter = starter + 1
    return blocks

def get_slice(text):
    pointer1 = random.randint(0, len(text)-1)
    pointer2 = random.randint(pointer1, pointer1+1500)
    return text[pointer1:pointer2],pointer2-pointer1

####################################################################################
#----------------INTRODUCING THE AMAZING STOCKY!!!!!!!!----------------------------#
####################################################################################

def stochastic_hill_climb(start_state, mutate, fitness, patience=10000, target=None, show_progress=False):
    # Generic stochastic hill climber.
    parent = start_state
    best = parent
    best_fitness = fitness(parent)
    counter = 0
    while counter < patience:
        child = mutate(parent)
        current_fitness = fitness(child)

        if current_fitness > best_fitness:
            parent = child
            best = child
            best_fitness = current_fitness
            counter = 0
            if show_progress:
                print(best_fitness)
            if target != None and best_fitness >= target:
                break
        else:
            counter += 1
    return best, best_fitness

def random_restart_hill_climb(state_generator, mutate, fitness, restarts=50, patience=10000,
                              target=None, show_progress=False):
    # Run multiple hill climbs and keep the best result.
    champion = None
    champion_score = float('-inf')
    for i in range(restarts):
        candidate, score = stochastic_hill_climb(
            state_generator(),
            mutate,
            fitness,
            patience,
            target,
            show_progress
        )
        if score > champion_score:
            champion = candidate
            champion_score = score
            if show_progress:
                print('\nNEW BEST FOUND!', champion_score)

        if target != None and champion_score >= target:
            break
    return champion, champion_score
