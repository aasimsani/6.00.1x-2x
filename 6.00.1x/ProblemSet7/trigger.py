import unittest
import sys


class NewsStory(object):
    def __init__(self,guid,title,subject,summary,link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):

        return self.guid

    def getTitle(self):
        

        return self.title

    def getSubject(self):

        return self.subject

    def getSummary(self):

        return self.summary

    def getLink(self):
        
        return self.link

class Trigger(object):

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """

        raise NotImplementedError     
        

class WordTrigger(Trigger):
    """docstring for WordTrigger"""
    def __init__(self,word):

        self.word = word.lower()

    def isWordIn(self,text):
        import re

        self.textlist = re.split(r'[;,!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~\s]\s*', text.lower())
        print self.word
        print self.textlist
        def subWordInrecur(word,textlist):
            try:
                if word == textlist[0]:
                    return True

                else:
                    return subWordInrecur(word,textlist[1:])
            except IndexError,e:

                return False

        return subWordInrecur(self.word,self.textlist)

class TitleTrigger(WordTrigger):

	def evaluate(self,story):

		self.story = story
		self.estr = story.getTitle()

		return TitleTrigger.isWordIn(self,self.estr)



koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
soda      = NewsStory('', 'Soft drinks are great', '', '', '')
pink      = NewsStory('', "Soft's the new pink!", '', '', '')
football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
caps      = NewsStory('', 'soft things are soft', '', '', '')

s1 = TitleTrigger('SOFT')
s2  = TitleTrigger('soft')
for trig in [s1, s2]:
    assertTrue(trig.evaluate(koala), "TitleTrigger failed to fire when the word appeared in the title")
    assertTrue(trig.evaluate(pillow), "TitleTrigger failed to fire when the word had punctuation on it")
    assertTrue(trig.evaluate(soda), "TitleTrigger failed to fire when the case was different")
    assertTrue(trig.evaluate(pink), "TitleTrigger failed to fire when the word had an apostrophe on it")
    assertTrue(trig.evaluate(football), "TitleTrigger failed to fire in the presence of lots of punctuation")
    assertTrue(trig.evaluate(caps), "TitleTrigger is case-sensitive and shouldn't be")
            
    assertFalse(trig.evaluate(microsoft), "TitleTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'")
    assertFalse(trig.evaluate(nothing), "TitleTrigger fired when the word wasn't really present in the title")

