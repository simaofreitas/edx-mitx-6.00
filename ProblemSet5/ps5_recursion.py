# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.

    aStr: a string
    returns: a reversed string
    """
    if aStr == "":
        return ""
    else:
        return aStr[len(aStr)-1] + reverseString(aStr[:len(aStr)-1])

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False

    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    elif word == "" and x != "":
        return False
    elif x[0] in word:
        return True and x_ian(x[1:], word[word.find(x[0]):])
    else:
        return False


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    """
    ### TODO.
    if len(text) < lineLength or " " not in text:
        return text
    else:
        empty = text[lineLength-1:].find(" ")
        return text[:lineLength+empty].strip() + "\n" + insertNewlines(text[lineLength+empty:].strip(),lineLength)

print insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
