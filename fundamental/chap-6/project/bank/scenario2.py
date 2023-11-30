from account import SavingAccount, CheckingAccount
from user import BankUser

user2 = BankUser("Brian", 900)

# 입출금 계좌에 $800
user2.deduct_money(800)
account1 = CheckingAccount(user2.get_name(), 800)
user2.add_account(account1)

# 6% 예금 계좌 $100
user2.deduct_money(100)
account2 = SavingAccount(user2.get_name(), 100, 0.06)
user2.add_account(account2)

try:
    account1.withdraw(800)
except ValueError:
    account1.update_limit(800)
    account1.withdraw(800)
finally:
    user2.add_money(800)

user2.get_assets()