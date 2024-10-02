import random, copy

print('Tic-Tac-Toe')

def drawBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O')
        letter = input('> ')

        #The first element in the player List is Player's Letter and Second letter is Computer's. if player enters 'X' that meaans List[0] = X and [1] is 'O
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'

def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or 
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or 
            (bo[2] == le and bo[4] == le and bo[6] == le))

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMoved(board):
    move = ''
    while not move in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your Next Move? (1-9)')
        move = input('> ')
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLatter = 'O'
    else:
        playerLatter = 'X'

    for i in range(0, 9):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(board, computerLetter):
                return i


    for i in range(0, 9):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLatter, i)
            if isWinner(board, playerLatter):
                return i

    move = chooseRandomMoveFromList(board, [1,3,5,7])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [0,2,6,8])


def isBoardFull(board):
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to TIC-TAC-TOE')

while True:
    theBoard = [' '] * 10

    playerLatter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst()
    print("The " + turn + 'will go first. ')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player':
            drawBoard(theBoard)
            move = getPlayerMoved(theBoard)
            makeMove(theBoard, playerLatter, move)
            if isWinner(theBoard, playerLatter):
                drawBoard(theBoard)
                print('Hooray! You have won the game! ')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tie! ')
                    break
                else:
                    turn = 'Computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You Lose .')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is Tie!')
                else:
                    turn = 'player'

        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('Y'):
            break
