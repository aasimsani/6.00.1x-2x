def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    import string

    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    retdic = {}

    for c in uc:
    	if (uc.index(c) + shift + 1) <= 24:
    		retdic[c] = uc[uc.index(c) + shift ]
    	else:
    		retdic[c] = uc[uc.index(c) + shift - 26 ]

    for c in lc:
    	if (lc.index(c) + shift + 1) <= 24:
    		retdic[c] = lc[lc.index(c) + shift ]
    	else:
    		retdic[c] = lc[lc.index(c) + shift - 26 ]


    return retdic



print buildCoder(3)
