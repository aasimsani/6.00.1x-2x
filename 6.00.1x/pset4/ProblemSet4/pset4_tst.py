hand = {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}
h = []
word = ""
def itword(h,wlist,z):
	try:
		if wlist[z] in h:
			return itword(h,wlist,z+1)
		pass
	except IndexError, e:
		return True
	else:
		return False
		pass

for letter in hand.keys():
        for j in range(hand[letter]):
             h.append(letter)    

wlist = []

for l in word:
	wlist.append(l)

wlist.sort()
h.sort()


print h
print itword(h,wlist,0)