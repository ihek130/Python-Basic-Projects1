import random
# Both of this variables are global
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   0   |
       |
       |
      ===''', '''
   +---+
   0   |
   |   |
       |
      ===''', '''
   +---+
   0   |
  /|   |
       |
      ===''', '''
   +---+
   0   |
  /|\  |
       |
      ===''', '''
   +---+
   0   |
  /|\  |
  /    |
      ===''', '''
   +---+
   0   |
  /|\  |
  / \  |
      ===''']

words = '''apple banana cat dog elephent frog grapes horse ink jackle keggle lemon
           mango nest orange python quest rabbit saturday toggle umberalla ven wolf
           yellow zebra'''.split()

def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)

    return wordlist[wordIndex]

def getBoard(correctLetters, missedLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed Letters")
    for letters in missedLetters:
        print(letters, end=' ')

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 

    for letters in blanks:
        print(letters, end=' ')
    print()
    
def getGuess(alreadyGuessed):
    while True:
        guess = ''
        print("\n Enter Your Guess...")
        guess = input('> ')
        if len(guess) != 1:
            print("Enter Guess Again")
        elif guess in alreadyGuessed:
            print("You already Guess that letter ")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter Guess in alphabats")
        else:
            return guess

def playAgain():
    print("Do you want to play again... Y/N ")
    play = input('> ')
    return play.lower().startswith('y')

print("HANGMAN")
correctWords = ''
missedWords = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    getBoard(correctWords, missedWords, secretWord)

    guess = getGuess(correctWords + missedWords)

    if guess in secretWord:
        correctWords = correctWords + guess
    
    foundAllLetters = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctWords:
            foundAllLetters = False
            break
    
    if foundAllLetters:
        print("Yes! You have won the game. Word was", secretWord)
        break
    else:
        missedWords = missedWords + guess

    if len(missedWords) == len(HANGMAN_PICS) - 1:
        getBoard(correctWords, missedWords, secretWord)
        print('You have run out of guesses!\nAfter ' + str(len(missedWords))
		+ ' missed guesses and ' + str(len(correctWords)) + ' correct guesses, the word was "' + secretWord + '"' )
        gameIsDone = True

	#Ask the player to play again
    if gameIsDone:
        if playAgain():
            missedWords = ''
            correctWords = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break

