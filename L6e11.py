animals = {'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon','baboon','baboon','baboon'], 'd': ['donkey', 'dog']}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    for i in aDict.keys():
    	if aDict[i] == max(aDict.values(), key=len):
    		return i

print biggest(animals)


    
