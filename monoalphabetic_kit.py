from linguistic_functions import *

HEB_ALPH = 'אבגדהוזחטיכלמנסעפצקרשת'
HEBREW_GEMATRIA = {
    'א': 1,   'ב': 2,   'ג': 3,   'ד': 4,   'ה': 5,
    'ו': 6,   'ז': 7,   'ח': 8,   'ט': 9,
    'י': 10,  'כ': 20,  'ך': 20,
    'ל': 30,
    'מ': 40,  'ם': 40,
    'נ': 50,  'ן': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,  'ף': 80,
    'צ': 90,  'ץ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400
} # I put this in for the gematria and semitic ciphers, which are included just for fun.
#!----TODO: find an alphabet for the Pigpen cipher ----!

def is_mono(text):
  # determines whether ciphertext is monoalphabetic
    ioc_text = IOC(text)
    #standard IOC = ~1.7
    frequencies = letter_freqs(text)
    fitness = find_cosine_angle(frequencies)
    if (ioc_text < 2 and ioc_text > 1.3) and (fitness < 0.8):
        # adjust these value to be stricter or less strict. I set them at a guess
        return True
    return False

def invert(key):
    # Generates the inverse of a scrambled alphabet key.
    inverse = ''
    for char in ALPHABET:
        inverse = inverse + ALPHABET[key.index(char)]
    return inverse

def mono_sub(cipher, key, encrypt=False):
    # The tofu-and-potatoes (I'm vegetarian) of the monoalphabetic cipher.
    # Problem: we rarely just 'know' the key.
    if not encrypt:
        key = invert(key)
    
    for char in ALPHABET:
        cipher = cipher.replace(char, key[ALPHABET.index(char)].lower())
    return cipher

def ancient_semitic_ciphers(text, method=0, alph=ALPHABET):
    text = clean(text)
    #Gematria is only for hebrew, and atbash and albam are not yet Heb-compatible.
    while method > 3 or method < 1: 
        method = int(input('Atbash - 1\nAlbam - 2\nGematria (beta) - 3\n-->'))
    if method == 1: # Atbash
        print('Succesfully decrypted with the Atbash cipher')
        return mono_sub(text, alph[::-1])
    elif method == 2: # Albam
        print('Succesfully decrypted with the Albam cipher')
        return mono_sub(text, alph[len(alph)//2:] + alph[:len(alph)//2])        
    else:
      #The gematria option
        print('Gematria only works for Hebrew text.')
        total = 0
        for char in text:
            if char in HEBREW_GEMATRIA:
                total += HEBREW_GEMATRIA[char]
        return 'The gematria of your text is' + str(total)
        
def affine(text):
    # implements the affine cipher on an English alphabet
    # the formula for affine ciphertext is ax + b
    valid_a = [1,3,5,7,9,11,15,17,19,21,23,25]
    for a in valid_a:
        for i in range(26):
            if (a * i) % 26 == 1:
                break
        for b in range(26):
            plain = ''
            for char in text:
                plain = plain + str(ALPHABET[(i*(ALPHABET.index(char) - b))%26])
            if X_squared_text(plain) < 100:
                return(plain)

def multiplicative(text, key, mode="decrypt"):
    # encrypts/decrypts the multiplicative cipher
    solved = ''
    keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if key not in keys:
        return ''
    if mode == 'decrypt':
        inv = pow(key, -1, 26)   
    for char in text:
        solved = solved + ALPH[(ALPH.index(char) * key)%26]
    return solved




