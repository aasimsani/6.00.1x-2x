secretWord= "lettuce"
lettersGuessed =  ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'e']
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if len(secretWord) == 1 and secretWord[0] in lettersGuessed:
        return True
    elif secretWord[0] in lettersGuessed:
        return isWordGuessed(secretWord[1:],lettersGuessed)
    else:
        return False

print isWordGuessed(secretWord,lettersGuessed)