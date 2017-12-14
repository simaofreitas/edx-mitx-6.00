from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for w in wordList
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(w, hand, wordList):
            # Find out how much making that word is worth
            tmp = getWordScore(w, HAND_SIZE)
            # If the score for that word is higher than your best score
            if tmp > maxScore:
                # Update your best score, and best word accordingly
                maxScore = tmp
                bestWord = w

    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    total = 0
    comchoice = ''
    while comchoice is not None:
        comchoice = compChooseWord(hand, wordList, n)
        print '\nCurrent hand:', displayHand(hand)
        if isValidWord(comchoice, hand, wordList):
            wordscore = getWordScore(comchoice, n)
            total += wordscore
            print '"'+ str(comchoice) + '"', 'earned', str(getWordScore(comchoice, n)) + ' points.', 'Total:', str(total), 'points'
            hand = updateHand(hand, comchoice)
        else:
            continue
    else:
        print "Total Score:", total
        
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    user_input = ''
    comlasthand = {}
    humanlasthand = {}
    lastplayer = None
    while user_input is not 'e':
        user_input = raw_input("Enter n to play a new hand, r to replay the last hand, e to end the game: ")
        if user_input is 'e':
            print 'Game ended!'
            break
        elif user_input is 'n':
            userinput = raw_input("Enter u for user play, c for comp play: ")
            if userinput is 'u':
                lastplayer = 'Human'
                humanlasthand = dealHand(HAND_SIZE)
                playHand(humanlasthand.copy(), wordList, HAND_SIZE)
            elif userinput is 'c':
                lastplayer = 'Comp'
                comlasthand = dealHand(HAND_SIZE)
                compPlayHand(comlasthand.copy(), wordList, HAND_SIZE)
            else:
                print 'Invalid Command'
        elif user_input is 'r' and lastplayer is 'Human':
            playHand(humanlasthand.copy(), wordList, HAND_SIZE)
        elif user_input is 'r' and lastplayer is 'Comp':
            compPlayHand(comlasthand.copy(), wordList, HAND_SIZE)
        elif user_input is 'r' and lastplayer is None:
            print 'You haven\'t played a hand yet, please play a hand.\n'
        else:
            print 'Invalid Command!'


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


