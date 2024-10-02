
import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU', 7: 'SHICHI', 8: 'HACHI', 9: 'KU', 10: 'JU'}

print("Cho-Han, by Al Sweigrat al@inventwithpython.com")

print('''In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number''')

purse = 5000

player1 = print('You have', purse, 'mon. How much do you bet? (or QUIT)')
response = ' '
while True:
    pot = input('> ')
    if pot.upper() == 'QUIT':
        print("Thanks for Playing ")
        sys.exit()
    elif not pot.isdecimal():
        print("Please, Enter a Number ")
    elif int(pot) > purse:
        print("You do not have Enough to make that bet")
    else:
        pot = int(pot)
        break

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print("The dealer swirls the cup and you hear the rattle of dice.")
print('''The dealer slams the cup on the floor, still covering the dice and 
      ask for your bet. ''')

print("CHO (even) or HAN *(odd) ?")
while True:
    bet = input('> ').upper()
    if bet != 'CHO' and bet != 'HAN':
        print('Please, Enter Either "CHO" or "HAN"')
        continue
    else:
        break

print("The dealer Lifts the cup to reveal: ")
print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
print('  ', dice1,' - ',dice2 )


rollisEven = (dice1 + dice2) % 2 == 0
if rollisEven:
    correctBet = 'CHO'
else:
    correctBet = 'HAN'

playerWon = bet == correctBet

if playerWon:
    print("You won! you take", pot, "mon")
    purse = purse + pot
    print('The House Collects a', pot // 10, 'mon fee')
    purse = purse - (pot // 10)
else:
    purse = purse - pot
    print('You lost!')


if purse == 0:
    print('You have run out of money!')
    print('Thanks for playing!')
    sys.exit()




