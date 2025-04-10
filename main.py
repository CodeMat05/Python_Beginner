from banking import BankAccount

TERMINATE, WITHDRAW, DEPOSIT, BALANCE, SUMMARY, WITHDRAW_SUMMARY = (0, 1, 2, 3, 4, 5)

def printMenu():
    print(f"\tEnter {WITHDRAW}: Withdraw")
    print(f"\tEnter {DEPOSIT}: Deposit")
    print(f"\tEnter {BALANCE}: Check Balance")
    print(f"\tEnter {SUMMARY}: Summary of Transactions")
    print(f"\tEnter {WITHDRAW_SUMMARY}: Summary of Withdraws")
    print(f"\tEnter {TERMINATE}: exit")


def main():
    account = BankAccount('Matmat')
    operation = BALANCE
    while operation != TERMINATE:
        printMenu()
        operation = int(input("Enter Operation code: "))
        if operation == WITHDRAW:
            account.withdrawAmount()
        elif operation == DEPOSIT:
            account.depositAmount()
        elif operation == BALANCE:
            account.checkBalance()
        elif operation == SUMMARY:
            account.printSummary()
        elif operation == WITHDRAW_SUMMARY:
            account.printWithdrawSummary()
        elif operation == TERMINATE:
            print('Good Bye')
        else:
            print("Invalid Operation")

if __name__ == '__main__':
    main()