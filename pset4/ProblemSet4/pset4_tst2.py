hand = {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}
word = "raz"

wdic = {}
for x in word:
	wdic[x] = wdic.get(x,0) +1

print hand
print wdic
clist =[]

for x in word:
	if x in hand.keys() and hand[x] >= wdic[x]:
		clist.append("True")
	else:
		clist.append("False")
def check(clist):
	if "False" in clist:
		return False
	else:
		return True


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    count = 0
    for letter in hand.keys():
        for j in range(hand[letter]):
            count += 1
    return count

print calculateHandlen(hand)