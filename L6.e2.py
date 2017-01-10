def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    n = ()
    for i in range(0,len(aTup)-1):
    	if i % 2 == 0:
    		n += (aTup[i],)
    return n

