def getGuessedWdord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
'''
    swlist = []
    for c in secretWord:
        swlist.append(c)
    swlist = sorted(swlist)
    lettersGuessed = sorted(lettersGuessed)
    prnt = []
    for c in range(0,len(secretWord)):
        prnt.append("_ ")
    for char in lettersGuessed:
        for ch in swlist: 
            if char == ch:
                prnt[swlist.index(ch)] = ch 
    return "".join(prnt)
''' 
def getGuessWord(secretWord,lettersGuessed):
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





print getGuessWord("apelle",['a','l'])


