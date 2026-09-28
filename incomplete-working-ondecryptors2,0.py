#Libraries
from linguistic_functions import (
    IOC, split_blocks, find_cosine_angle,
    get_slice, ALPHABET, tetra_fitness,
    get_text, is_mono, get_fittest)
from polyalphabetic_kit import (
    determine_period,
    polyalphabetic_substitution)
from monoalphabetic_kit import mono_sub
import os, random, sys

# functions
class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, data):
        for f in self.files:
            f.write(data)

    def flush(self):
        for f in self.files:
            f.flush()
            
def get_uname():
    # Creates a unique filename for the user.
    if not os.path.exists('./summaries'):
        os.makedirs('./summaries')
        
    with open('ranked_dict.txt','r') as file:
        file = file.read().splitlines()
    code = random.choice(file)
    while os.path.exists('./summaries/'+code+'.txt'):
        code = ''.join([random.choice(ALPHABET) for i in range(5)])
    return code

def sinkov_spikes(text):
    #T/F whether sinkov's method creates a spike.
    avgs = []
    lengths = []
    for j in range(1, 20):
        blocks = split_blocks(text, j)
        avg_ioc = sum(IOC(block) for block in blocks)
        avg_ioc /= len(blocks)
        lengths.append(j)
        avgs.append(avg_ioc)
    return (max(avgs) - sum(avgs)/len(avgs))>0.35
    
def determine_type(text):
    # uses a range of analyses to determine method
    # used to encode ciphertext
    ioc = IOC(text)
    tetragram_fitness = tetra_fitness(text)
    cosine = find_cosine_angle(text)
    
    if ioc >= 1.3:
        if is_mono(text):
            return 4 #mono
        elif tetragram_fitness < 0.006:
            return 3 #transpo
        else:
            return 2 #plaintext
    elif sinkov_spikes(text):
        return 1 #poly
    else:
        return 0 #random
    
def mono_solver(text, threshold=0.02, restarts=20, patience=10000):
    # Dictionary attack first
    try:
        with open("ranked_dict.txt", "r") as file:
            words = file.read().splitlines()
        results = []
        for key in gen(words):
            plaintext = mono_sub(text, key)
            results.append((tetra_fitness(plaintext), plaintext, key))

        best_score, best_plaintext, best_key = max(results)

        if best_score >= threshold:
            return best_plaintext, best_key, best_score

    except FileNotFoundError:
        pass

    # Hill climb if dictionary attack failed
    champion_plaintext = ''
    champion_key = ''
    champion_score = float('-inf')

    for _ in range(restarts):

        parent = list(ALPHABET)
        random.shuffle(parent)
        parent = ''.join(parent)

        parent_plaintext = mono_sub(text, parent)
        parent_score = tetra_fitness(parent_plaintext)

        counter = 0

        while counter < patience:
            if counter % 100 == 0:
                print(counter, parent_score)

            child = list(parent)

            x = random.randrange(26)
            y = random.randrange(26)

            child[x], child[y] = child[y], child[x]
            child = ''.join(child)

            child_plaintext = mono_sub(text, child)
            child_score = tetra_fitness(child_plaintext)

            if child_score > parent_score:
                parent = child
                parent_score = child_score
                parent_plaintext = child_plaintext
                counter = 0
            else:
                counter += 1

        if parent_score > champion_score:
            champion_score = parent_score
            champion_plaintext = parent_plaintext
            champion_key = parent

    return champion_plaintext, champion_key, champion_score

types_array = ['random','polyalphabetic','plaintext','transposition','monoalphabetic']
code = get_uname()
log = './summaries/' + code + '.txt'
sys.stdout = Tee(sys.stdout, log)
sys.stderr = Tee(sys.stderr, log)
print('Welcome to Iridium1\'s decryptor2.0!' +
      f'\nYou are user {code}. At the end of this conversation, you can find a' +
      f'\nsummary of data used in our conversation at /summaries/{code}.txt.')

text = get_text()
method = determine_type(text)
print('This text appears to be', types_array[method], end='.')
print(
    f'''
You entered the following text:
\'{text}\'
Summary:

Most Likely Cipher Type: {types_array[method]}

Index of Coincidence (IoC): {round(IOC(text),3)}
Measures how uneven the letter distribution is.
Lower values often indicate polyalphabetic encryption.

Tetragram Fitness: {round(tetra_fitness(text),3)}
Measures how closely the text\'s four-letter patterns resemble those of normal English.
Higher values indicate a closer match to English.

Cosine Similarity: {round(find_cosine_angle(text),3)}
Measures how closely the text's letter frequencies match standard English letter frequencies.
Higher values indicate a closer match.
''')
if method == 1:
    print(poly_hill_climb(text))
#everything below this is for testing purposes
# 
# with open("brown_corpus_no_spaces.txt","r") as file:
#     corpus = file.read()
# 
# for i in range(20):
#     viggy = vigenere(get_slice(corpus)[0], ''.join([random.choice(ALPHABET) for i in range(random.randint(5, 20))]))
#     print(sinkov_spikes(get_slice(corpus)[0]))
#     print('viggy', sinkov_spikes(viggy))
    
