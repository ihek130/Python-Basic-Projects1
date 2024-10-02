'''Hangman Game Beginner project # 2'''

import random

Hangman_Pics = ['''
 +---+
  |   |
      |
      |
      |
      |
=========

  +---+
  |   |
  O   |
      |
      |
      |
=========

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========   

''']

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra'''.split()


def getRandomWord(wordsList):
    wordsIndex = random.randint(0, len(words))
    return wordsList[wordsIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(Hangman_Pics[len(missedLetters)])
    print()

    print("Missed Letters \n")
    for letter in missedLetters:
        print(letter, end='')

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetter:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    print("Correct Letters \n")
    for letter in blanks:
        print(correctLetters, end='')
    
    print()


def Guess(alreadyGuessed):
    guess = ''
    while True:
        print("Enter Guess ")
        guess = input('> ')
        guess = guess.lower()
        if len(guess) != 1:
            print("Please! Enter one Word at a time")
        elif not guess.isalpha():
            print("Guess should be alphabatic Character")
        elif guess in alreadyGuessed:
            print("You already Guessed that. insert different Charatcer")
        else: 
            return guess
        
print("H A N G M A N")
missedLetter = ''
correctLetter = ''
secretWord = getRandomWord(words)
gameisFinished = False


while True:
    displayBoard(missedLetter, correctLetter, secretWord)

    guess = Guess(correctLetter + missedLetter)

    if guess in secretWord:
        correctLetter = correctLetter + guess

    fooundAll = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetter:
            fooundAll = False
            break
        if fooundAll:
            print("Yes! You won the Game. Secret Word is", guess)
    else:
        missedLetter = missedLetter + guess

    
    if len(missedLetter) > len(Hangman_Pics):
        displayBoard(missedLetter, correctLetter, secretWord)
        print("You ran out of Guesses")
        gameisFinished = True
        break



choice = print("Do you want to play again..")
if choice.lower().startswith('n'):
    gameisFinished = True
