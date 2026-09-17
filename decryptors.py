from linguistic_functions import clean, gen, X_squared_text, parse
def dict_attack(text, method): # methods: 1 - mono_sub, 2+ - more to add...
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
      if X_squared_text(plain) < mini:
        mini = X_squared_text(plain)
        print(parse(plain.upper()), '\n' + key)
