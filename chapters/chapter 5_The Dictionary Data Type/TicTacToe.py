# before AI
import random
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def userinput():
    print ('place your chioce ')
    
    string = input()

    return string

print ('Your are  X and Computer O')
print ('============================')

keys = list(theBoard.keys())
print(keys)
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    theBoard[random.choice(keys)] = 'O'
printBoard(theBoard)