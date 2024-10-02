import random

MAX_DIGITS = 3
MAX_GUESSES = 10

def getNumber():
    num = list(range(10))
    random.shuffle(num)
    secretNum = ''
    for i in range(MAX_DIGITS):
        secretNum += str(num[i])
    return secretNum

def getClues(secretNum, guess):
    if secretNum == guess:
        print("Congrats! You've got it")
    
    clues = []
    for i in range(len(guess)):
        if secretNum[i] == guess[i]:
            clues.append('Fermi')
        elif secretNum[i] == guess:
            clues.append('Pico')
        else:
            return "Begals"

def isOnlyDigits(num):
    if num == ' ':
        return False

    for i in num:
        if i not in '0123456789'.split():
            return False
        return True


print("The Begals Deduction Game ")

print('I am thinking of a %s-digit number. Try to guess what it is.' %
 (MAX_DIGITS))
print('The clues I give are...')
print('When I say: That means:')
print(' Bagels None of the digits is correct.')
print(' Pico One digit is correct but in the wrong position.')
print(' Fermi One digit is correct and in the right position.')

while True:
    
    secNum = getNumber()

    print("I have thought up a number. You have 10 Guesses to get it.")
    guessTaken = 1
    while guessTaken <= MAX_GUESSES:
        guess = ""
        while len(guess) != MAX_DIGITS or not isOnlyDigits(guess):
            print("Guess #", guessTaken)
            guess = input('> ')

        print(getClues(secNum, guess))
        guessTaken = guessTaken + 1 

        if guess == secNum:
            break
        if guessTaken > MAX_GUESSES:
            print("You ranout of Guesses ")

    print("Do you want to play again ")
    if not input().lower().startswith('y'):
        break
       









