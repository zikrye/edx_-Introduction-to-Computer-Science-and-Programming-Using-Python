# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for w in secretWord:
        if w not in lettersGuessed:
            return False
    return True
        
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = []
    for w in secretWord:
        if w not in lettersGuessed:
            result.append('_ ')
        else:
            result.append(w)
    return ''.join(result)

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))


import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
# solution 1
#    str = string.ascii_lowercase
#    for l in lettersGuessed:
#        if l in str:
#            str = str.replace(l, '')
#    return str

# solution 2
    str = list(string.ascii_lowercase)
    for l in lettersGuessed:
        if l in str:
            str.remove(l)
    return ''.join(str)
            
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']        
print(getAvailableLetters(lettersGuessed))      
        
        

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
    print('Welcome to the game Hangman!')
    secretWord = chooseWord(wordlist)
    length = len(secretWord)
    print('I am thinking of a word that is', length, 'letters long.')
    print('-------------')
    num = 8
    # mistakesMade = 0
    lettersGuessed = []
    
    while num >= 1:
        print('You have', num, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed), end = '')
        guess = input('Please guess a letter: ').lower()
        lettersGuessed.append(guess)

        if guess not in lettersGuessed:          
            if guess in secretWord:                
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                if isWordGuessed(secretWord, lettersGuessed) is True:
                    print('Congratulations, you won!')
                    break
            else:
                num -= 1
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                if num == 0:
                    print('Sorry, you ran out of guesses. The word was', secretWord + '. ')
        else:
            print('Ops! You have already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            
        

        
    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
