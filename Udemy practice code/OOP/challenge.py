'''
For this challenge, create a bank account that has two attributes:
1. owner name
2. balance

and two methods:
1. deposit
2. withdraw

Note: withdrawls may not exceed the available balance.
'''

class Account():


    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        

    def withdraw(self,amount):
        if amount>self.balance:
            print('Funds is insufficient. {} cannot be withdrawn'.format(amount))
            return False
        else:
            self.balance = self.balance - amount
            print(f'{amount} has been deducted from your bank account.')
            return True


    def deposit(self,amount):
        if amount < 0:
            print(f'Amount is invalid')
        else:
            self.balance = self.balance + amount

    def __str__(self):
        return f"{self.owner}'s balance is {self.balance}"
    

acc1 = Account('Nithin',2000)

print('Account owner: {}\nAccount balance: {}\n'.format(acc1.owner,acc1.balance))
print(acc1)
acc1.withdraw(3000)
acc1.withdraw(100)

print('Account owner: {}\nAccount balance: {}\n'.format(acc1.owner,acc1.balance))
print(acc1)
acc1.deposit(2000)
acc1.withdraw(3000)

print('Account owner: {}\nAccount balance: {}\n'.format(acc1.owner,acc1.balance))
print(acc1)