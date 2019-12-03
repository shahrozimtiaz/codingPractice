import numpy as np
import string

words = open("words.txt","r").readlines()
wordsUsed = {}

boardSize = 15
board = np.zeros([boardSize,boardSize],str)
alph = list(string.ascii_lowercase)

def boardFilled():
    for row in range(boardSize):
        for col in range(boardSize):
            if board[row][col] == "":
                return False
    return True

def fillBoard():
    for row in range(boardSize):
        for col in range(boardSize):
            if board[row][col] == "":
                board[row][col]=np.random.choice(alph)
    return True

def printBoard():
    board_str = "---------------\n"
    for row in range(boardSize):
        for col in range(boardSize):
            if(board[row][col]!=""):
                board_str += str(board[row][col]) + " "
            else:
                board_str += "- "
                # board_str += str(row)+","+str(col)+" "
        board_str += "\n"
    print(board_str)

if __name__ == "__main__":
    # printBoard()
    words = np.random.choice(words,replace=False,size=1000)
    wordIndex = 0
    dirs = ['up','down','left','right','diagRightDown','diagRightUp','diagLeftDown','diagLeftUp']
    # while(boardFilled()!=True):
    x=12
    attempts = 0
    while(len(wordsUsed)<x):
        attempts +=1
        postion = [np.random.choice(boardSize), np.random.choice(boardSize)]
        if(attempts==32):
            # print('reset')
            wordIndex+=1
            attempts=0
        word = words[wordIndex].lower().replace("\n","")
        # word = 'COOL'
        # dir = 'diagLeftUp'
        wordLen = len(word)
        # for lkj in range(1):
        dirs = np.random.choice(a=dirs,size=len(dirs),replace=False)
        clear = True
        # print('dirs: ',dirs)
        for dir in dirs:
            # print(dir)
            if dir == 'up':
                if postion[0] - (wordLen-1) < 0:
                    # print('failedUP')
                    continue
                for r, ch in zip(range(postion[0], postion[0] - wordLen, -1), word):
                    if board[r][postion[1]] != "" and board[r][postion[1]]!=ch:
                        # print('failedUP')
                        clear = False
                        break
                if clear:
                    for r,ch in zip(range(postion[0],postion[0]-wordLen,-1),word):
                        board[r][postion[1]] = ch
                        wordsUsed[word] = 1
                    attempts=0
                    wordIndex+=1
                    break
            elif dir == 'down':
                if postion[0] + (wordLen-1) >= boardSize:
                    # print('failedDOWN')
                    continue
                for r, ch in zip(range(postion[0], postion[0] + wordLen), word):
                    if board[r][postion[1]] != "" and board[r][postion[1]]!=ch:
                        # print('failedDOWN')
                        clear = False
                        break
                if clear:
                    for r, ch in zip(range(postion[0], postion[0] + wordLen), word):
                        board[r][postion[1]] = ch
                        wordsUsed[word] = 1
                    attempts = 0
                    wordIndex+=1
                    break
            elif dir == 'left':
                if postion[1] - (wordLen-1) < 0:
                    # print('failedLeft')
                    continue
                for c, ch in zip(range(postion[1], postion[1] - wordLen, -1), word):
                    if board[postion[0]][c] != "" and board[postion[0]][c]!=ch:
                        # print('failedLeft')
                        clear = False
                        break
                if clear:
                    for c, ch in zip(range(postion[1], postion[1] - wordLen, -1), word):
                        board[postion[0]][c] = ch
                        wordsUsed[word] = 1
                    attempts = 0
                    wordIndex+=1
                    break
            elif dir == 'right':
                if postion[1] + (wordLen-1) >= boardSize:
                    # print('failedRight')
                    continue
                for c, ch in zip(range(postion[1], postion[1] + wordLen), word):
                    if board[postion[0]][c] != "" and board[postion[0]][c]!=ch:
                        # print('failedRight')
                        clear = False
                        break
                if clear:
                    for c, ch in zip(range(postion[1], postion[1] + wordLen), word):
                        board[postion[0]][c] = ch
                        wordsUsed[word] = 1
                    attempts = 0
                    wordIndex+=1
                    break
            elif dir == 'diagRightDown':
                if postion[0] + (wordLen-1) >= boardSize or postion[1] + wordLen >= boardSize:
                    # print('failedDRD')
                    continue
                for ri,cj,ch in zip(range(postion[0],postion[0] + wordLen),range(postion[1], postion[1] + wordLen),word):
                    if board[ri][cj] != ""and board[ri][cj]!=ch:
                        # print('failedDRD')
                        clear = False
                        break
                if clear:
                    for ri,cj,ch in zip(range(postion[0],postion[0] + wordLen),range(postion[1], postion[1] + wordLen),word):
                        board[ri][cj] = ch
                        wordsUsed[word] = 1
                    attempts = 0
                    wordIndex+=1
                    break
            elif dir == 'diagRightUp':
                if postion[0] - (wordLen-1) < 0 or postion[1] + wordLen >= boardSize:
                    # print('failedDRU')
                    continue
                for ri,cj,ch in zip(range(postion[0],postion[0] - wordLen,-1),range(postion[1], postion[1] + wordLen),word):
                    if board[ri][cj] != "" and board[ri][cj]!=ch:
                        # print('failedDRU')
                        clear = False
                        break
                if clear:
                    for ri,cj,ch in zip(range(postion[0],postion[0] - wordLen,-1),range(postion[1], postion[1] + wordLen),word):
                        board[ri][cj] = ch
                        wordsUsed[word] = 1
                    attempts = 0
                    wordIndex+=1
                    break
            elif dir == 'diagLeftDown':
                if postion[0] + (wordLen-1) >= boardSize or postion[1] - (wordLen-1) < 0:
                    # print('failedDLD')
                    continue
                for ri,cj,ch in zip(range(postion[0],postion[0] + wordLen),range(postion[1], postion[1] - wordLen,-1),word):
                    if board[ri][cj] != "" and board[ri][cj]!=ch:
                        # print('failedDLD')
                        clear = False
                        break
                if clear:
                    for ri,cj,ch in zip(range(postion[0],postion[0] + wordLen),range(postion[1], postion[1] - wordLen,-1),word):
                        board[ri][cj] = ch
                        wordsUsed[word] = 1
                    attempts = 0
                    wordIndex+=1
                    break
            elif dir == 'diagLeftUp':
                if postion[0] - (wordLen-1) < 0 or postion[1] - (wordLen-1) < 0:
                    # print('failedDLU')
                    continue
                for ri,cj,ch in zip(range(postion[0],postion[0] - wordLen,-1),range(postion[1], postion[1] - wordLen,-1),word):
                    if board[ri][cj] != "" and board[ri][cj]!=ch:
                        # print('failedDLU')
                        clear = False
                        break
                if clear:
                    for ri,cj,ch in zip(range(postion[0],postion[0] - wordLen,-1),range(postion[1], postion[1] - wordLen,-1),word):
                        board[ri][cj] = ch
                        wordsUsed[word] = 1
                    attempts = 0
                    wordIndex+=1
                    break
    fillBoard()
    printBoard()
    print('words used:')
    for key in wordsUsed.keys():
        print("",key)