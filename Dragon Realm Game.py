import random

print(''' Dragon Realm Game''')

def dispIntro():
     print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight''')


def ChooseCave():
     cave = ''
     while cave != '1' or cave != '0':
          print("Which Cave will you go into? (1 or 2)")
          cave = input("> ")

          return cave

def checkCave(ChooseCave):
     print('You approch the cave...')
     print('It is dark and spooky...')
     print('A large dragon jumps out in front of you! He opens his jaws and....')

     friendlyCave = random.randint(1, 2)

     if friendlyCave == str(ChooseCave):
          print('Gives you his treasure! ')
     else:
          print("Gobbles you down in one bite! ")
     
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'Y' or playAgain == 'y':
     dispIntro()
     Cavee = ChooseCave()
     checkCave(Cavee)


     print("Do you want to play again ('yes or no)")
     playAgain = input('> ')     
