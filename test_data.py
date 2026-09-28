from linguistic_functions import *
from monoalphabetic_kit import is_mono
from polyalphabetic_kit import determine_period
import random

if __name__ == "__main__":
    text_to_write = 'Linguistic Data for Testing Purposes\n'

    with open('Brown_corpus_no_spaces.txt', 'r') as file:
        text = file.read()
        # IoC
        text_to_write = text_to_write + 'Index of coincidence for a given plaintext length\n'
        for i in range(6):
            bit = get_slice(text)
            text_to_write = text_to_write + str(IOC(bit[0])) + ',' + str(bit[1]) + '\n'
            
        #X-squared
        text_to_write = text_to_write + 'X-squared characteristic \n'
        for i in range(6):
            bit = get_slice(text)
            text_to_write = text_to_write + str(X_squared_text(bit[0])) + ',' + str(bit[1]) + '\n'
            
        #monogram frequencies
        text_to_write = text_to_write + 'Monogram frequencies for a given length (alphabetical order) \n'
        for i in range(6):
            bit = get_slice(text)
            text_to_write = text_to_write + str(letter_freqs(bit[0])) + ',' + str(bit[1]) + '\n'
            
        #cosine angle
        text_to_write = text_to_write + 'Cosine angle between plaintext and slices \n'
        for i in range(6):
            bit = get_slice(text)
            text_to_write = text_to_write + str(find_cosine_angle(letter_freqs(bit[0]))) + ',' + str(bit[1]) + '\n'
            
        #parsing - why not?
        text_to_write = text_to_write + 'Parsed text for a given length \n'
        for i in range(6):
            bit = get_slice(text)
            text_to_write = text_to_write + parse(bit[0]) + ',' + str(bit[1]) + '\n'
            
        #is monoalphabetic
        text_to_write = text_to_write + 'Identified as monoalphabetic \n'
        for i in range(6):
            bit = get_slice(text)
            text_to_write = text_to_write + str(is_mono(bit[0])) + ',' + str(bit[1]) + '\n'
            
        #sinkov's test for probable keylength
        text_to_write = text_to_write + 'Probable keylength \n'
        for i in range(6):
            bit = get_slice(text)
            text_to_write = text_to_write + str(determine_period(bit[0])) + ',' + str(bit[1])+ '\n'
        
    with open('Tester_data.txt','w') as file2:
        file2.write(text_to_write)
        print('Text written to Tester_data.txt')

    if input('Press any key to view text, otherwise enter ') != '':
        print(text_to_write)
    print('Goodbye!')
        
