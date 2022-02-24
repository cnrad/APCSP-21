# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, ommitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0

  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a two-word password
def two_word(password):
    words = get_dictionary()
    guesses = 0

    for w in words:
        guesses += 1
        if password.startswith(w) == True:
            for w2 in words:
                guesses += 1
                if (f'{w}{w2}' == password):
                    return True, guesses
        
    return False, guesses

    
def two_words_and_digit(password):
    words = get_dictionary()
    guesses = 0

    for j in range(10):
        guesses += 1
        if password.startswith(f'{j}'):
            for w in words:
                guesses += 1
                if password.startswith(f'{j}{w}') == True:
                    for w2 in words:
                        guesses += 1
                        if password == f'{j}{w}{w2}':
                            return True, guesses

    for w in words:
        if password.startswith(w) == True:
            for w2 in words:
                guesses += 1
                if (password.startswith(f'{w}{w2}')):
                    for i in range(10):
                        if f'{w}{w2}{i}' == password:
                            return True, guesses
        
    return False, guesses


def two_words_digit_character(password):
    words = get_dictionary()
    guesses = 0
    digits = '~!@#$%^&*()_-+={[}]|\:<>'

    for j in range(10):
        guesses += 1
        if password.startswith(f'{j}'):
            for w in words:
                guesses += 1
                if password.startswith(f'{j}{w}') == True:
                    for w2 in words:
                        guesses += 1
                        if password.startswith(f'{j}{w}{w2}'):
                            for d in digits:
                                if password == f'{j}{w}{w2}{d}':
                                    return True, guesses

    for w in words:
        if password.startswith(w) == True:
            for w2 in words:
                guesses += 1
                if (password.startswith(f'{w}{w2}')):
                    for i in range(10):
                        if password.startswith(f'{w}{w2}{i}'):
                            for d in digits:
                                if password == f'{w}{w2}{i}{d}':
                                    return True, guesses
        
    return False, guesses
