class SavingsAccount:
    def _init_(self, annual_rate, saving_balance):
        self.saving_balance=annual_rate
        self.annual_inter_rate=saving_balance

    def MonthlyInterest(self):
        monthly_interest = self.saving_balance * self.annual_inter_rate / 1200
        self.saving_balance+= monthly_interest
    def modifyInterestRate(self,new_inter_rate):
        self.annual_inter_rate=new_inter_rate

saver1=SavingsAccount(5,2000)
saver2=SavingsAccount(5,3000)
saver1.MonthlyInterest()
saver2.MonthlyInterest()
print(f" Balance for saver 1(with rate {saver1.annual_inter_rate}): {saver1.saving_balance}")
print(f" Balance for saver 2(with rate {saver2.annual_inter_rate}): {saver2.saving_balance}")
saver1.modifyInterestRate(7)
saver2.modifyInterestRate(7)
saver1.MonthlyInterest()
saver2.MonthlyInterest()
print(f"New balance for saver 1(with rate {saver1.annual_inter_rate}): {saver1.saving_balance}")
print(f"New balance for saver 2(with rate {saver2.annual_inter_rate}): {saver2.saving_balance}")