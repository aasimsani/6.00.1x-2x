import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 

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


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    encrypted = []
    for char in text:
    	if char in string.ascii_lowercase or char in string.ascii_uppercase:
    		encrypted.append(coder[char])
    	else:
    		encrypted.append(char)

    return ''.join(encrypted)


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    print applyCoder(text, buildCoder(shift))




applyShift("hello", 3)