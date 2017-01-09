aList= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]




def flatten(S):
    if S == []:
        return S
    if type(S[0]) == list:
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

print flatten(aList)