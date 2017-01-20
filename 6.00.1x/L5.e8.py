def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    midIndex = len(aStr)/2
    midChar = aStr[midIndex]
    aStr = ''.join(sorted(aStr))
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    if char == midChar:
        return True
    if char < midChar:
        return isIn(char,aStr[:midIndex])
    else:
        return isIn(char,aStr[midIndex:])



