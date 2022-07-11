class Bank_Account:
    def __init__(self,account_no):
        self.account_no = account_no
    def print(self):
        print(f"Your Account numbver is {self.account_no}.")
class Saving_Account(Bank_Account):
    def __init__(self,account_no,min_bal,int_rate):
        super().__init__(account_no)
        self.min_bal=min_bal
        self.int_rate=int_rate
    def print(self):
        super().print()
        print(f"Minimum balance is {self.min_bal} and Interest rate is {self.int_rate} ")
class Current_Account(Bank_Account):
    def __init__(self,account_no,withdrawl_limit):
        super().__init__(account_no)
        self.withdrawl_limit = withdrawl_limit
    def print(self):
        super().print()
        print(f"withdrawl limit is {self.withdrawl_limit}")
s1=Saving_Account(4444444444445,20000,0.03)
s1.print()
c1=Current_Account(4544444444442,50000)
c1.print()
