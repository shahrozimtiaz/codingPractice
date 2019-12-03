def count(mineField,N,row,col):
    if row >= N or row < 0 or col>=N or col<0:
        return 0
    d = recurrCount(mineField.copy(),1,N,row,col)
    return d

def recurrCount(mineField,d,N,row,col):
    mineField[row][col]=-1
    if(row-1>=0 and mineField[row-1][col]!=-1 and mineField[row-1][col]==0): #left
        d += 1 + recurrCount(mineField,0,N,row-1,col)
    if(row+1<N and mineField[row+1][col]!=-1 and mineField[row+1][col]==0): #right
        d += 1 + recurrCount(mineField, 0, N, row+1, col)
    if(col-1>=0 and mineField[row][col-1]!=-1 and mineField[row][col-1]==0): #up
        d += 1 + recurrCount(mineField, 0, N, row, col-1)
    if(col+1<N) and mineField[row][col+1]!=-1 and mineField[row][col+1]==0: #down
        d += 1 + recurrCount(mineField, 0, N, row, col+1)
    return d

def tests():
    mineField = [
        [1,0,1],
        [1,0,1],
        [0,0,0]
    ]
    test1 = count(mineField,len(mineField),0,0)
    if test1 == 6:
        print('test1 passed.. Result:',test1)
    else:
        print('test1 failed. Expected 3.. actual',test1)

if __name__ == "__main__":
    tests()