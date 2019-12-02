class Bank:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.accounts = {}

    def __str__(self):
        return 'Bank Name: {}, Balance: ${}, Accounts #: {}'.format(self.name,self.balance,len(self.accounts))

    class Account:
        def __init__(self,name,bank,balance=0):
            self.name = name
            self.bank = bank
            self.balance = balance
            self.bank.accounts[self.name] = self
            self.bank.balance += balance

        def addMoney(self,amount):
            self.balance += amount
            self.bank.balance += amount

        def takeMoney(self,amount,reason='no reason'):
            self.balance -= amount
            self.bank.balance -= amount
            print('${} were taken from {} for {}. New balance: ${}'.format(amount,self.name,reason,self.balance))

        def transfer(self,account2,amount):
            if(self.balance>=amount):
                self.balance -= amount
                self.bank.balance -= amount
                account2.balance += amount
                account2.bank.balance += amount
            else:
                print('{} with a balance of ${} does not have enough funds to transfer ${} to {}'.format(self.name,self.balance,amount,account2.name))

        def __str__(self):
            return 'Account Name: {}, Balance: ${}, Bank: {}'.format(self.name,self.balance,self.bank.name)

if __name__ == '__main__':
    boa = Bank('Bank of America')
    bbt = Bank('BB&T')

    leah = bbt.Account('leah',bbt,200)
    shahroz = boa.Account('shahroz',boa,10)
    gadget = boa.Account('gadget',boa,1000000)

    leah.transfer(shahroz,10)
    leah.addMoney(10)
    shahroz.transfer(leah,3000000)
    leah.transfer(shahroz,201)

    leah.takeMoney(12,'Netflix')

    print('----------------------------------------------')
    print(boa)
    print(bbt)
    print('----------------------------------------------')
    print(leah)
    print(shahroz)
