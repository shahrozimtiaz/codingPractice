import sudokuSolver as ss
import random

def generateBoard(numBlanks):
    board = [[0]*9 for i in range(9)]
    boards = ss.sudokuSolver(board)
    board = boards[0]
    for n in range(numBlanks):
        r = random.randint(0,8)
        c = random.randint(0,8)
        while board[r][c] == 0:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
        board[r][c] = 0
    return board

def countBlanks(board):
    count = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c]==0:
                count+=1
    return count

if __name__ == '__main__':
    board = generateBoard(10)
    ss.printBoard(board)