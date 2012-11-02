# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dict = {}
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    for l in range(len(upper)):
        dict[upper[l]] = upper[(l+shift)%len(upper)]
    for l in range(len(lower)):
        dict[lower[l]] = lower[(l+shift)%len(lower)]
    return dict
    
print buildCoder(3)

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    final = ""

    for l in text:
        if not (l in string.punctuation or l == " " or l in str(range(10))):
            final += coder[l]
        else:
            final += l

    return final

print applyCoder("Hello12, World!", buildCoder(3))
print applyCoder("Khoor, Zruog! ", buildCoder(23))

    

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
    coder = buildCoder(shift)

    return applyCoder(text,coder)

print applyShift('This is a test.', 8)    

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO

    #Variable for the best cipher and best match and current match
    bestMatch = 0
    realWords = 0
    #Range from 0 to 26, i
    for i in range(26):
        #current match = 0
        currentMatch = 0
        #Transform text with i shift
        converted = applyShift(text,i)
        #split results
        lista = converted.split(' ')
        #check if valid word
        for w in lista:
            # if valid
            if isWord(wordList,w):
                #increment current match
                currentMatch += 1
        #if current match is > than best match
        if currentMatch > realWords:
            #replace best match with current match and change best cipher
            bestMatch = i
            realWords = currentMatch
    #return best chipher
    return bestMatch


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    text = getStoryString()
    bestMatch = findBestShift(loadWords(), text)
    return applyShift(text, bestMatch)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    decryptStory()

s = 'Pmttw, ewztl!'
print findBestShift(wordList, s)

print decryptStory()