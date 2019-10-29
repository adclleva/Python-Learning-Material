# data-structures using tic tac toe

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
 # Because you created a data structure to represent a tic-tac-toe board and wrote code in printBoard() to interpret that data structure,
 # you now have a program that “models” the tic-tac-toe board. You could have organized your data structure differently
 # (for example, using keys like 'TOP-LEFT' instead of 'top-L'), but as long as the code works with your data structures, you will have a correctly working program.

# we can use the type() method to get the data type of something

type(42)
# <class 'int'>
type('Hi')
# <class 'str'>
type('3.14')
# <class 'str'>
type([0,1])
# <class 'list'>
type({'key': 'value'})
# <class 'dict'>