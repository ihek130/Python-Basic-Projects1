print("Carrot in Box, by Al Sweigrat al@inventwithpython.com")

import random

print("Human player 1, enter your name: ")
player1 = input("> ")

print("Human player 2, enter your name: ")
player2 = input("> ")

print('''HERE ARE TWO BOXES: 

  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print(player1 + "Red Box ^ ")
print(player2 + "Gold Box ^ ")

print(player1 + "You have Red Box in front of you ")
print(player2 + "You have Gold Box in front of you ")
print("Press Enter to continue ")
print()
print("When " + player2 + "has Closed their Eyes, press Enter...")
print(player1 + "Here is Inside of your Box")

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
    ___VV____
   |   VV    |
   |   VV    |
   |___||____|    __________
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
  (carrot!)''')
    print(player1, player2)
else:
    print('''
    _________
   |         |
   |         |
   |_________|    __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
 (no carrot!)''')
    print(player1, player2)

input("Press Enter to continue...")

print('\n' * 100)
print(player1 + ', tell ' + player2 + ' to open their eyes. ')
input("Press Enter to continue....")
print()


print(f"{player1} say one of following sentences to {player2} ")
print("1) There is a carrot in my box.")
print("2) There is not a carrot in my box.")
print()

input("Press Enter to  Continue...")

print()

print(player2 + "Do you want to swap the box with "+ player1 + " Press Y/N ")
while True:
    response = input("> ").upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print("Please Enter Yes / No ")
    else:
        break

firstBox = "RED "
secondBox = "GOLD"

if response.startswith("Y"):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''HERE ARE TWO BOXES:

  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(player1, player2)

print("Press Enter to reveal the Winner ")
print()

if carrotInFirstBox:
    print('''
    ___VV____
   |   VV    |
   |   VV    |
   |___||____|    __________
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
  (carrot!)''')

else:
    print('''
    ___ ____
   |         |
   |         |       
   |___  ____|    __||______
  /         /|   /  ||     /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
  (carrot!)''')

if carrotInFirstBox:
    print(f"{player1} is the Winner! ")
else:
    print(f"{player2} is the Winner! ")

print("Thanks for Playing....")
    
    
    
    

    

    





