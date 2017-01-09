def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    wdic = {}
    for x in word:
        wdic[x] = wdic.get(x,0) +1

        
        def recVword(wdic,hand,x):
                if x > len(word-1):
                    return True
                elif word[x] in hand.keys() and hand[word[x]] >= wdic[word[x]:
                    return recVword(hand,wdic,x+1)
                else:
                    return False

        if word in wordList and recVword(wdic,hand,0) == True:
            print "Working"

        else:
            return False
    


