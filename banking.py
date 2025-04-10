
class BankAccount:
    def __init__(self, accountName):
        self.name = accountName
    
    accountBalance = 0
    transactions = [] #other way = list()

    def depositAmount(self):
        deposit = float(input('Enter amount to deposit: '))
        if deposit <= 0:
            print('Invalid Amount')
        else:
            self.accountBalance += deposit
            self.transactions.append(('deposit', deposit))

    def withdrawAmount(self):
        withdraw = float(input('Enter amount to withdraw: '))
        if withdraw > self.accountBalance:
            print('Invalid Amount')
        else:
            self.accountBalance -= withdraw
            self.transactions.append(('withdraw', withdraw))

    def checkBalance(self):
        print(f'Your present Balance is: P {self.accountBalance}')
        self.transactions.append(('check-balance', self.accountBalance))

    def printSummary(self):
        self.printTransaction(self.transactions)

    def printTransaction(self, operations):
        printables = map(lambda trans: f'{trans[0]}, {trans[1]}', operations)
        counter = 1
        for line in printables:
            print(f'{counter}: {line}')
            counter += 1

    def printWithdrawSummary(self):
        # def checkIfWithdraw(trans):
        #     return trans[0] == 'withdraw'
        withdraws = filter(
            lambda trans: trans[0] == 'withdraw', 
            self.transactions 
        )
        self.printTransaction(withdraws)
        
