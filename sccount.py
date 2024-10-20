class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit
    def debit(self, amount):
        self.balance -= amount
        print("Debitted amount:", amount)

    #credit
    def credit(self, amount):
        self.balance += amount
        print("Credited amount:", amount)

acc1 = Account(1000, 101)
print("account balance: ", acc1.balance)
print("account number: ", acc1.account_no)

acc1.debit(100)
acc1.credit(200)