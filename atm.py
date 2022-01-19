class atm(object):
    def __init__(self, CashWithdrawl, BalanceEnquiry):
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry

    def account(self):
        account = input("enter you credit card number:- ")
        print("thank you!!")

    def Withdrawl(self):
        Withdrawl = input("how much money do you want form your account:-")
        print("thank you!!")

yourAccount = atm("$2000","$20000")

print(yourAccount.Withdrawl())