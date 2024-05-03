class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created. \n Balance = ${
              self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount'{self.name}' balance =${
              self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()  # Calls the get balnce method hence same output functionallity

# This method has not been called hence it is not processed at the time since in the oop_project.py file we write Dave.withdraw(10) and not Dave.ViableTransaction
    def viableTransaction(self, amount):
        # after being called in the withdraw method value assigned in withdraw is used here
        if self.balance >= amount:
            return  # exiting of the method when requirements are met
        else:
            # When raise is encountered, the normal flow of the program is interrupted. Python immediately stops executing the current code and starts looking for a piece of code that knows how to handle the specific error you raised.
            raise BalanceException(
                f"\nSorry account'{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):  # amount has been assigned a new value in withdraw method
        try:
            # calling of the viableTransaction method with the amount in withdraw
            self.viableTransaction(amount)
            # after exiting the withdraw method(through return) the comp continues fro here without calling the self visble transaction again since it is not a loop
            self.balance = self.balance - amount
            print(f"\nWithdraw complete")
            self.getBalance()
            # When the raising execution occurs python will go to the exception handler below.
        except BalanceException as error:  # as error, enables you to gain access to information about the exception that occurred hence goes back and prints the info within the balanceException error handler
            # hence the information is printed here
            print(f"\nWithdraw interrupted {error}")

    def transfer(self, amount, account):
        try:
            print('\n***********\n\nBeginning Transfer..🔔🔔')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!!!💵💵')
        except BalanceException as error:
            print(f'\nTransfer interrupted.❌❌ {error}')


class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete")
        self.getBalance()


# init is used here because so that we can be able to initialize the fee for withdrawing
class savingsAcct(InterestRewardAcct):
    # if you do this(def __init__(self))this will suggest that only one requirement is needed since it overwrites info of the superclass
    def __init__(self, initialAmount, acctName):
        # This is done so as to maintain functionallity of the other classes
        super().__init__(initialAmount, acctName)
        self.fee = 5  # addition of the required fee

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdrawal complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted:{error}")
