def isVowel(char):
    char = char.lower()
    if char == 'a' or char == 'i' or char == 'e' or char == 'o' or char == 'u':
    	return True
    else:
    	return False



for char in 'aeioun':
	print isVowel(char)