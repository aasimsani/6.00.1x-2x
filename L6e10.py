animals = {'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog']}

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for i in animals.keys():
    	for e in animals[i]:
    		count += 1
    return count

howMany(animals)
