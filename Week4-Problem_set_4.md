
# Classic Wordgame like Scrabble #

This game is a lot like Scrabble or Words With Friends, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

# Dealing

A player is dealt a hand of n letters chosen at random (assume n=7 for now).

The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

Some letters may remain unused (these won't be scored).

# Scoring

The score for the hand is the sum of the scores for each word formed.

The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).



```python
# The 6.00 Word Game


import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

HAND_SIZE = 15
n=HAND_SIZE

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    A=[]
    for i in word:
        
        A.append(SCRABBLE_LETTER_VALUES[i])
    points=sum(A)*len(word)
    if len(word)==n:
        return points+50
    elif len(word)==0:
        return 0  
    else:
        return points



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    copy=dict(dict(hand))
    for i in word:
        copy[i]=copy.get(i,0)-1
    return (copy)
        



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word in wordList:
        for i in word:
            copy1=dict(dict(hand))
            if all (k in copy1 for k in word):
                for i in word:
                    copy1[i]=int(copy1.get(i,0))-1
                return all(int(value) >= 0 for value in copy1.values())
            else:
                return False
    else:
        return False

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    total=sum(hand.values())
    return total


def playHand(hand, wordList, n):   
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    totalscore=[]
    total=sum(totalscore)       
    # As long as there are still letters left in the hand:
    while any(int(value) > 0 for value in hand.values())==True:
        # Display the hand
        print("Current Hand: " , end='') 
        displayHand(hand)
        # Ask user for input
        word=str(input("Enter word, or a '.' to indicate that you are finished: "))       
        # If the input is a single period:
        if word=='.':      
            # End the game (break out of the loop)
            print ("Goodbye! Total score: "+ str(total) + " points.")
            break           
        # Otherwise (the input is not a single period):
        else :      
            # If the word is not valid:
            if isValidWord(word, hand, wordList)!=True:          
                # Reject invalid word (print a message followed by a blank line)
                print ("Invalid word, please try again.")
                print()
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalscore.append(getWordScore(word, n))
                total=sum(totalscore)
                print (str(word) + " earned "+ str(getWordScore(word, n)) + " points. Total: "+ str(total) + " points")
                print()
                # Update the hand 
                hand=updateHand(hand, word)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if all(int(value) == 0 for value in hand.values())==True:
        return ("Run out of letters. Total score: "+ str(total) + " points.")

#
# Problem #5: Playing a game
# 
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    hand={}
    #define input command
    x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
    #enter a loop till user doesnt want to end
    while x!='e':
        # when user wants to deal a new hand
        if x=='n':
            hand=dealHand(n)
            playHand(hand, wordList, n)
            x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        
        # when user gives invalid input
        elif x not in ('e','n','r'):
            print("Invalid command.")
            x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        
        # when user wants to replay hand
        else:
            # if user inputs r for first round
            if  hand=={}:
                print ("You have not played a hand yet. Please play a new hand first!")
                x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))

            else:
                
                hand=hand
                playHand(hand, wordList, n)
                x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))


wordList = loadWords()
playGame(wordList)

```

    Loading word list from file...
       83667 words loaded.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: i e e e a b b n n l w f t d v 
    Enter word, or a '.' to indicate that you are finished: bible
    bible earned 45 points. Total: 45 points
    
    Current Hand: e e a n n w f t d v 
    Enter word, or a '.' to indicate that you are finished: teen
    teen earned 16 points. Total: 61 points
    
    Current Hand: a n w f d v 
    Enter word, or a '.' to indicate that you are finished: fan
    fan earned 18 points. Total: 79 points
    
    Current Hand: w d v 
    Enter word, or a '.' to indicate that you are finished: .
    Goodbye! Total score: 79 points.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    

# Part B


```python
from ps4a import *
import time

n=HAND_SIZE
#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
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
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (sum(hand.values()) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

#play hand function redefined
def playHand(hand, wordList, n):
        totalscore=[]
        total=sum(totalscore)
        while any(int(value) > 0 for value in hand.values())==True:
            print("Current Hand: " , end='') 
            displayHand(hand)

            print()
            word=str(input("Enter word, or a '.' to indicate that you are finished: "))
            if word=='.':
                print ("Goodbye! Total score: "+ str(total) + " points.")
                break
            
            else :
                if isValidWord(word, hand, wordList)!=True:
                    print ("Invalid word, please try again.")
                    print()
                else :
                    totalscore.append(getWordScore(word, n))
                    total=sum(totalscore)
                    print (str(word) + " earned "+ str(getWordScore(word, n)) + " points. Total: "+ str(total) + " points")
                    print()
                    hand=updateHand(hand, word)
        if all(int(value) == 0 for value in hand.values())==True:
            return ("Run out of letters. Total score: "+ str(total) + " points.")


#
# Problem #6: Playing a game
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
    n=HAND_SIZE
    # TO DO... <-- Remove this comment when you code this function
    hand={}
    
    #Asks the user to input 'n' or 'r' or 'e'.
    x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
    
    #If the user inputs 'e', immediately exit the game.
    while x!='e':
        
        # If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again
        if x not in ('e','n','r'):
            print("Invalid command.")
            x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        
        elif x=='r':
            if hand=={}:   
                print ("You have not played a hand yet. Please play a new hand first!")
                x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
            else:
                y=str(input("Enter u to have yourself play, c to have the computer play: "))
                # If the user inputs anything that's not 'c' or 'u', keep asking them again
                while y not in ('u','c'):
                    print("Invalid command.")
                    y=str(input("Enter u to have yourself play, c to have the computer play: "))
                #Switch functionality based on the above choices.* If the user inputted 'u', let the user play the game
                #with the selected hand, using playHand.If the user inputted 'n', play a new (random) hand.
                if (y =='u'):
                    hand=hand
                    playHand(hand, wordList, n)
                    x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
                else:
                    hand=hand
                    compPlayHand(hand, wordList, n)
                    x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        else:
            
            y=str(input("Enter u to have yourself play, c to have the computer play: "))
                # If the user inputs anything that's not 'c' or 'u', keep asking them again
            while y not in ('u','c'):
                
                print("Invalid command.")
                y=str(input("Enter u to have yourself play, c to have the computer play: "))
                #Switch functionality based on the above choices.* If the user inputted 'u', let the user play the game
                #with the selected hand, using playHand.If the user inputted 'n', play a new (random) hand.
            
            if (y =='u'):
                hand=dealHand(n)
                playHand(hand, wordList, n)
                x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
            else:
                hand=dealHand(n)
                compPlayHand(hand, wordList, n)
                x=str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
            

wordList = loadWords()

playGame(wordList)



```

    Loading word list from file...
       83667 words loaded.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Enter u to have yourself play, c to have the computer play: u
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: mic
    Invalid word, please try again.
    
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: com
    Invalid word, please try again.
    
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: mock
    Invalid word, please try again.
    
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: om
    Invalid word, please try again.
    
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: bic
    Invalid word, please try again.
    
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: .
    Goodbye! Total score: 0 points.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Enter u to have yourself play, c to have the computer play: u
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: dom
    Invalid word, please try again.
    
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: mo
    Invalid word, please try again.
    
    Current Hand: i o m k b d c 
    
    Enter word, or a '.' to indicate that you are finished: .
    Goodbye! Total score: 0 points.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Enter u to have yourself play, c to have the computer play: c
    Current Hand:  u i n k h c p 
    Total score: 0 points.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    


```python

```
