import string

lettersGuessed = ['a','b','c']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    str1 = string.ascii_lowercase
    strl =[]
    for char in str1:
    	strl.append(char)
    for c in lettersGuessed:
    	if c in strl:
    		strl.remove(c)

    return ''.join(strl)

print getAvailableLetters(lettersGuessed)
