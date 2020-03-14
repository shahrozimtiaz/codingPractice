import sodokuGenerator as sg
import random
import copy
import json

hard_board1=[
    [3,0,6,5,0,8,4,0,0],
    [5,2,0,0,0,0,0,0,0],
    [0,8,7,0,0,0,0,3,1],
    [0,0,3,0,1,0,0,8,0],
    [9,0,0,8,6,3,0,0,5],
    [0,5,0,0,9,0,6,0,0],
    [1,3,0,0,0,0,2,5,0],
    [0,0,0,0,0,0,0,7,4],
    [0,0,5,2,0,6,3,0,0]
]

hard_board2 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

hard_board3 = [
    [0, 0, 2, 9, 8, 0, 5, 0, 0],
    [4, 0, 0, 0, 7, 0, 0, 1, 3],
    [0, 3, 9, 6, 0, 4, 0, 7, 0],
    [2, 0, 0, 0, 5, 6, 4, 0, 0],
    [8, 4, 0, 3, 0, 0, 2, 0, 1],
    [9, 0, 7, 0, 0, 1, 0, 8, 6],
    [6, 0, 0, 7, 0, 5, 1, 3, 0],
    [0, 9, 1, 4, 0, 0, 0, 0, 5],
    [0, 2, 0, 0, 3, 0, 6, 0, 8]
]

def rowCheck(board,r,val):
    for c in range(len(board[r])):
        if board[r][c] == val:
            return False
    return True

def colCheck(board,c,val):
    for r in range(len(board)):
        if board[r][c] == val:
            return False
    return True

def gridCheck(board,r,c,val):
    sr,sc = r,c
    while sr%3!=0 or sc%3!=0:
        if sr%3!=0:
            sr-=1
        else:
            sc-=1
    for r in range(sr,sr+3):
        for c in range(sc,sc+3):
            if board[r][c] == val:
                return False
    return True

def valueCheck(board,r,c,val):
    return rowCheck(board,r,val) and colCheck(board,c,val) and gridCheck(board,r,c,val)

def findNextPosition(board,r,c):
    for r in range(r,len(board[r])):
        for c in range(c,len(board)):
            if board[r][c] == 0:
                return r,c
        c = 0
    return -1,-1

def printBoard(board):
    print('#########################')
    print('-------------------------')
    for r in range(len(board)):
        row = '| '
        for c in range(len(board[r])):
            if (c+1)%3==0:
                row += str(board[r][c]) + ' | '
            else:
                row += str(board[r][c]) + ' '
        print(row.replace('0','_'))
        if (r + 1) % 3 == 0:
            print('-------------------------')

def _rowCheck(board,r,c):
    for cc in range(len(board[r])):
        if board[r][cc] == board[r][c] and c!=cc:
            print('row check failed')
            return False
    return True
def _colCheck(board,r,c):
    for rr in range(len(board)):
        if board[rr][c] == board[r][c] and rr!=r:
            print('col check failed')
            return False
    return True
def _checkGrid(board, r, c):
    sr, sc = r, c
    while sr % 3 != 0 or sc % 3 != 0:
        if sr % 3 != 0:
            sr -= 1
        else:
            sc -= 1
    for rr in range(sr, sr + 3):
        for cc in range(sc, sc + 3):
            if board[rr][cc] == board[r][c] and (rr!=r and cc!=c):
                print('grid check failed')
                return False
    return True

def _checkValue(board,r,c):
    return _rowCheck(board,r,c) and _colCheck(board,r,c) and _checkGrid(board,r,c)

def checkInputBoard(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c]!=0 and not _checkValue(board,r,c):
                print('invalid input board')
                return False
    return True

def checkOutputBoard(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c]==0 or not _checkValue(board,r,c):
                print('invalid output board')
                return False
    return True

def sudokuSolver(board,r=0,c=0,solutionBoards=[]):
    if len(solutionBoards) > 1:
        return
    r,c = findNextPosition(board,r,c)
    if r == -1:
        solutionBoards.append(copy.deepcopy(board))
        return
    shuffled_range = list(range(1, 10))
    random.shuffle(shuffled_range)
    for v in shuffled_range:
        if valueCheck(board,r,c,v):
            board[r][c]=v
            sudokuSolver(board,r,c,solutionBoards)
            board[r][c]=0
    return solutionBoards if len(solutionBoards)>0 else None

def loadBoard(n):
    file = open('sudokuProblems.txt','r')
    lines = file.readlines()
    return json.loads(lines[n])

if __name__ == '__main__':
    file = open('sudokuProblems.txt','a+')
    board = sg.generateBoard(39)
    printBoard(board)
    if checkInputBoard(board):
        boards = sudokuSolver(board)
        print(len(boards))
        printBoard(boards[0]) if board and checkOutputBoard(boards[0]) else print('no solution')
        print('possible solution:',len(boards))

    if input('save board to file? y/n \n') == 'y':
        file.write(json.dumps(board)+'\n')
