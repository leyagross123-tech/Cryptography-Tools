from linguistic_functions import split_blocks, IOC, parse, gen
from monoalphabetic_kit import mono_sub
from matPlotLib import pyplot as plt

def determine_period(text):
  #sinkov's test
  avgs = []
  lengths = []
  for i in range(1, 20):
    blocks = split_blocks(text, i)
    avg_ioc = sum(rc.IOC(block) for block in blocks) / len(blocks)
    lengths.append(i)
    avgs.append(avg_ioc)

    if input('Press 'q' to opt out of viewing a graph of key lengths\n>> ').upper() != 'Q':
        plt.plot(lengths, avgs, marker='+')
        plt.xlabel("Key Length")
        plt.ylabel("Average IOC")
        plt.title("Sinkov Test")
        plt.grid(True)
        plt.show()
    
    return lengths[avgs.index(max(avgs))]

def poly(text, alphabets):
    # this is the literal definition of a polyalphabetic cipher.
    # whilst not as typical a cipher as, say, vignere, this function is
    # still useful for other functions.
    new_text = ''
    alphanumber = 0
    for char in text:
        new_text = new_text + mono_sub(char, alphabets[alphanumber])
    alphanumber += 1
    if alphanumber == len(key_alphabets):
        alphanumber = 0
    return parse(new_text.upper())

def beaufort_shifter(text, key):
    # The beaufort shift is like a backward vignere.
    # encryption and decryption are the same
    # cipher (c) = k (key letter) - p (plaintext) + 26
    result = ''
    index = 0
  
    for char in text:
        k = key[index]
        c = ALPHABET.index(char)
        p = (ALPHABET.index[k] - c) % 26
        result = result + ALPHABET[p]
        index += 1
        if index == len(key):
          index = 0
    return result

def vignere(text, key):
    # decrypts the basic vignere cipher.
    alphas = []
    for char in key:
        alphas.append(gen(key, 'L'))

    return poly(alphas)
        
        
    
        
