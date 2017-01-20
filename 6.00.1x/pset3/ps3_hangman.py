# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
lettersGuessed =[]
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

def getGuessedWord(secretWord,lettersGuessed):
    prnt = []
    freq = {}
    for x in secretWord:
        freq[x] = freq.get(x,0) + 1
    for x in secretWord:
        if x not in lettersGuessed:
            freq[x] = freq.get(x,0)-1
            prnt.append('_')
        else:
            prnt.append(x)
    return ''.join(prnt)



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
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    count = 8
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    print "Welcome to  the game, Hangman!"
    print "I am thinking of a word that is ", len(secretWord), " letters long." , secretWord
    print "-------------"
    while count > 0:
        if isWordGuessed(secretWord,lettersGuessed) == True:
            print "Congratulations, you won!"
            break
        elif isWordGuessed(secretWord,lettersGuessed) == False:
            print "You have ", count, " guesses left."
            print "Available letters: ", getAvailableLetters(lettersGuessed)
            g = raw_input("Please guess a letter: ").lower()
            if g in secretWord and g not in lettersGuessed:
                lettersGuessed.append(g)
                print "Good guess: ", getGuessedWord(secretWord,lettersGuessed)
            elif g in lettersGuessed:
                print "Oops! You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed)
            elif g not in secretWord:
                lettersGuessed.append(g)
                count -= 1
                print "Oops! That letter is not in my word: ", getGuessedWord(secretWord,lettersGuessed)
            print "-------------"
    if count == 0:
        print "Sorry, you ran out of guesses. The word was", secretWord




# When you've completed your hangman function, uncomment these two lines
# and round this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

