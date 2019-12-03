class Stock:
    def __init__(self,action,numOfShares,pricePerShare):
        self.action = action
        self.numOfShares = numOfShares
        self.pricePerShare = pricePerShare

def hardInput():
    data = []
    stock1 = Stock('buy', 10, 5)
    data.append(stock1)
    stock2 = Stock('buy', 6, 6)
    data.append(stock2)
    stock3 = Stock('sell', 12, 7)
    data.append(stock3)
    stock4 = Stock('buy', 13, 8)
    data.append(stock4)
    stock5 = Stock('sell', 2, 3)
    data.append(stock5)
    stock6 = Stock('sell', 10, 2)
    data.append(stock6)
    return data

def sell(data):
    lastSoldOut = 0
    for i in range(len(data)):
        if data[i].action == 'sell':
            sellStock = data[i]
            numToSell = sellStock.numOfShares
            income = sellStock.numOfShares * sellStock.pricePerShare
            originalCost = 0
            for j in range(lastSoldOut,i,1):
                currStock = data[j]
                if currStock.action == 'buy':
                    if currStock.numOfShares >= numToSell:
                        originalCost += numToSell * currStock.pricePerShare
                        currStock.numOfShares = currStock.numOfShares-numToSell
                        break
                    else:
                        numToSell = numToSell - currStock.numOfShares
                        originalCost += currStock.numOfShares * currStock.pricePerShare
                        currStock.numOfShares = 0
                        lastSoldOut = j
            if(income-originalCost<0):
                print('Sold {} shares with INCOME of ${} and ORIGINAL COST of ${}. LOSS: ${}'.format(sellStock.numOfShares,income,originalCost,abs(income-originalCost)))
            else:
                print('Sold {} shares with INCOME of ${} and ORIGINAL COST of ${}. Profit: ${}'.format(sellStock.numOfShares,income,originalCost,abs(income-originalCost)))

if __name__ == '__main__':
    data = hardInput()
    sell(data)
