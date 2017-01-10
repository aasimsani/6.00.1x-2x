import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):

        self.shift = shift
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase
        retdic = {}

        for c in uc:
            if (uc.index(c) + self.shift + 1) <= 24:
                retdic[c] = uc[uc.index(c) + self.shift ]
            else:
                retdic[c] = uc[uc.index(c) + self.shift - 26 ]

        for c in lc:
            if (lc.index(c) + self.shift + 1) <= 24:
                retdic[c] = lc[lc.index(c) + self.shift ]
            else:
                retdic[c] = lc[lc.index(c) + self.shift - 26 ]


        return retdic

    

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift

        '''
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase

        text = self.message_text

        enc = []

        for char in text:
            if char in lc:
                if (lc.index(char) + shift + 1) <= 24:

                    enc.append(lc[lc.index(char) + shift])
                else:

                    enc.append(lc[lc.index(char) + shift - 26])

            elif char in uc:
                if (uc.index(char) + shift + 1) <= 24:

                    enc.append(uc[uc.index(char) + shift])

                else:

                    enc.append(uc[uc.index(char) + shift - 26])

            else:
                enc.append(char)


        return ''.join(enc)

                    
                





class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = Message.build_shift_dict(self,self.shift)
        self.message_text_encrypted = Message.apply_shift(self,self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()
        
        

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted



    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,self.shift)
        self.message_text_encrypted = Message.apply_shift(self,self.shift)
        


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        
        1. Set the maximum number of real words found to 0.
2. Set the best shift to 0.
3. For each possible shift from 0 to 26:
    4. Shift the entire text by this shift.
    5. Split the text up into a list of the individual words.
    6. Count the number of valid words in this list.
    7. If this number of valid words is more than the largest number of
       real words found, then:
        8. Record the number of valid words.
        9. Set the best shift to the current shift.
    10. Increment the current possible shift by 1. Repeat the loop
       starting at line 3.
11. Return the best shift.
        '''
        rwords = 0
        bshift = 0

        for es in range(0,26):

            t = CiphertextMessage.apply_shift(self,es)
            ts = t.split()
            vwords = 0
            for w in ts:
                if w in self.valid_words:
                    vwords += 1

            if vwords > rwords:
                rwords = vwords
                bshift = es



        return bshift,CiphertextMessage.apply_shift(self,bshift)




 





        



#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 3)
print 'Expected Output: khoor'
print 'Actual Output:', plaintext.get_message_text_encrypted()
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print 'Expected Output:', (24, 'hello')
print 'Actual Output:', ciphertext.decrypt_message()




def decrypt_story():
    return CiphertextMessage(get_story_string()).decrypt_message()



print decrypt_story()