import string

WORDLIST_FILENAME = "words.txt"

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 

    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    retdic = {}

    for c in uc:
    	if (uc.index(c) + shift + 1) <= 24:
    		retdic[c] = uc[uc.index(c) + shift ]
    	else:
    		retdic[c] = uc[uc.index(c) + shift - 26 ]

    for c in lc:
    	if (lc.index(c) + shift + 1) <= 24:
    		retdic[c] = lc[lc.index(c) + shift ]
    	else:
    		retdic[c] = lc[lc.index(c) + shift - 26 ]


    return retdic


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    encrypted = []
    for char in text:
    	if char in string.ascii_lowercase or char in string.ascii_uppercase:
    		encrypted.append(coder[char])
    	else:
    		encrypted.append(char)

    return ''.join(encrypted)


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return  applyCoder(text, buildCoder(shift))






def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    rlwrds = 0
    bshift = 0
    for s in range(0,26):
    	string = applyShift(text,s)

    	strlist = string.split(' ')

    	numwords = 0

    	for word in strlist:
    		if isWord(wordList, word) == True:
    			numwords += 1

    	if numwords > rlwrds:
    		rlwrds = numwords
    		bshift = s
    
    return applyShift(text, bshift)





wordList = loadWords()


text = "Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon yx dro czeb yp k wywoxd dy rovz myfob kx sxceppsmsoxdvi zvkxxon rkmu. Ro rkc loox boqscdobon pyb mvkccoc kd WSD dgsmo lopybo, led rkc bozybdonvi xofob zkccon k mvkcc. Sd rkc loox dro dbknsdsyx yp dro bocsnoxdc yp Okcd Mkwzec dy lomywo Tkmu Pvyboi pyb k pog xsqrdc okmr iokb dy onemkdo sxmywsxq cdenoxdc sx dro gkic, wokxc, kxn odrsmc yp rkmusxq."

z = applyShift(text, -3)

print findBestShift(wordList,z)
