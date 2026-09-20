from linguistic_functions import clean, gen, X_squared_text, parse
options_list = ['caesar','monoalphabetic substitution']
def dict_attack(text, method): # methods: 1 - mono_sub, 2 - vigenere, 3+ - more to add...
  text = clean(text)
  mini = 100 # the threshhold X-squared. Below this it's almost certainly plaintext.
  # get dictionary
  file = open('ranked_dict.txt','r').read().split('\n')
  for word in file:
      word = word.strip()
      if word == '':
          continue
      key = gen(word)
      if method == '1':
        plain = mono_sub(text, key)
      elif method == '2':
        
      if X_squared_text(plain) < mini:
        mini = X_squared_text(plain)
        print(parse(plain.upper()), '\n' + key)


print('Hello and welcome to The Grand Decryptor, by Iridium1.')
print('Enter the name of the cipher you wish to decrypt.')

choice = input('>> ')
while choice not in options_list:
	print(choice for choice in options_list)
	choice = input('>> ')
choice = options_list.index(choice)

if choice == 1:
	#caesar menu
elif choice == 2:
	#meh
  
