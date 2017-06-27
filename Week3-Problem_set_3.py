
# coding: utf-8

# # Classic Wordgame Hangman #
# 
# The second player will always be the computer, who will be picking a word at random.

# In[4]:

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "C:/Users/swapn/Downloads/Analytics/EDX/Intro2Python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
lettersGuessed=[]

#helper functions defined to be used in the program

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    len(secretWord)
    count=0
    for i in secretWord:
        if i in lettersGuessed:
            count+=1
    return count==len(secretWord)  


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word=""
    for i in secretWord:
        if i in lettersGuessed:
            word+=str(i)
        else:
            word+=str(" _ ")
    return (word) 


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lg=set(lettersGuessed)
    A=''.join([c for c in string.ascii_lowercase if c not in lg ])
    return(A)



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is " + str(len(secretWord))+" letters long")
    print("-----------")
    guessesleft=8
    while guessesleft!=0:
        
        print("You have "+ str(guessesleft)+" guesses left")
        print("Available Letters: " + str(getAvailableLetters(lettersGuessed)))
        x=str(input("Please guess a letter: "))
        if x in secretWord:  
            if x in lettersGuessed:
                print ("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed)))
                print("-----------")
            else:
                lettersGuessed.append(x)

                print ("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
                print("-----------")
                if isWordGuessed(secretWord, lettersGuessed)==True:
                    print ("Congratulations, you won!")
                    break
                    
            
        else:
            
            if x in lettersGuessed:
                print ("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed)))
                print("-----------")
            else:
                lettersGuessed.append(x)
                mistakesMade=0
                print ("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
                print("-----------")
                mistakesMade+=1
                guessesleft-=mistakesMade
    if guessesleft==0:
        
        print("Sorry, you ran out of guesses. The word was "+str(secretWord)+".")    

hangman(secretWord)


# In[ ]:



