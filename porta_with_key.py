#porta cipher
import linguistic_functions as lf
import monoalphabetic_kit as mono

#generating a tableau
is_euro = input('Default American porta. Enter E for European\n>> ').upper() == 'E'
amer = [lf.ALPHABET[i] + lf.ALPHABET[i+1] for i in range(0, 26, 2)]
euro = [amer[0]] + amer[:0:-1]
tableau = {}
if is_euro:
    key_pairs = euro
else:
    key_pairs = amer
for pair in key_pairs:
    p = key_pairs.index(pair) - 13
    upper = mono.caesar('NOPQRSTUVWXYZ',[p],encrypt=True,alph='NOPQRSTUVWXYZ')
    lower = [''] * 13
    for i in range(13):
        letter = upper[i]
        lower[lf.ALPHABET.index(letter) - 13] = lf.ALPHABET[i]

    tableau[pair] = upper + ''.join(lower)
key_tableau = {}

for pair in tableau:
    for letter in pair:
        key_tableau[letter] = tableau[pair]
#the function itself
def porta_cipher(ciphertext, keyword):
    key_index = 0
    new_text = ''
    for char in ciphertext:
        new_text = new_text + mono.mono_sub(char, key_tableau[keyword[key_index]])
        key_index += 1
        if key_index == len(keyword):
            key_index = 0
    return new_text
#decryption
ciphertext = lf.get_text()
keyword = lf.clean(input('Enter the keyword used for encryption, d for dictionary attack.\n>> '))
if keyword == 'D':
    with open('ranked_dict.txt','r') as file:
        file = file.read().splitlines()
    for word in file:
        decrypt = porta_cipher(ciphertext, word)
        if 'welli' in decrypt:
            print(word, '->', lf.parse(decrypt),'\n\n')
else:
    print(porta_cipher(ciphertext, keyword))