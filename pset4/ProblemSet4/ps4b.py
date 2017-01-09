from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compvalidW(word, hand):
    wrdic = {}
    for x in word:
        wrdic[x] = wrdic.get(x,0) +1

    colist =[]

    for x in word:
        if x in hand.keys() and hand[x] >= wrdic[x]:
            colist.append("True")
        else:
            colist.append("False")
    if check(colist) == True:
        return True
    else: 
        return False

def compChooseWord(hand, wordList, n):
    """f
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    def compvalidW(word, hand):
        wrdic = {}
        for x in word:
            wrdic[x] = wrdic.get(x,0) +1

        colist =[]

        for x in word:
            if x in hand.keys() and hand[x] >= wrdic[x]:
                colist.append("True")
            else:
                colist.append("False")
        if check(colist) == True:
            return True
        else: 
            return False
    mscore = 0

    # Create a new variable to store the best word seen so far (initially None) 
    bword = "None" 

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        if compvalidW(word, hand) == True:

        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth
            score = getWordScore(word,n)

            # If the score for that word is higher than your best score
            if score > mscore:

                # Update your best score, and best word accordingly
                bword = word
                mscore = score
        else:
            pass

    # return the best word you found.
    return bword


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    ctscore = 0
    while calculateHandlen(hand) > 0:
        print "Current Hand: ",
        displayHand(hand)
        word = compChooseWord(hand,wordList,n)
        if word == "None":
            break
        else:
            ctscore += getWordScore(word,n)
            print "\"",word,"\""," earned ",getWordScore(word,n), "points. Total: ", ctscore, " points"
            print

            hand = updateHand(hand, word)
    print "Total score: ", ctscore, "points."


#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      P
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    end = 0
    hand = ''
    while end == 0:
        choice = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        if choice == 'e':
            break
        if choice == 'n':
            hand = dealHand(HAND_SIZE)
            while end == 0:
                choice2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if choice2 == 'u':
                    print
                    playHand(hand,wordList,HAND_SIZE)
                    break
                elif choice2 == "c":
                        compPlayHand(hand,wordList,HAND_SIZE)
                        break
                else:
                    print "Invalid command!"
        elif choice == 'r':
            if hand == '':
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                while end == 0:
                    choice2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if choice2 == 'u':
                        print
                        playHand(hand,wordList,HAND_SIZE)
                        break
                    elif choice2 == "c":
                        print
                        compPlayHand(hand,wordList,HAND_SIZE)
                        break
                    else:
                        print "Invalid command!"
#"
        else:
            print "Invalid Input!"

 

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
