class BankUser:
    def __init__(self, name, money):
        self.__accounts = []
        self.__name = name
        self.__money = money
    
    def get_name(self):
        return self.__name

    def add_account(self, account):
        self.__accounts.append(account)

    def get_accounts(self):
        for account in self.__accounts:
            account.info()

    def add_money(self, amount):
        self.__money += amount

    def deduct_money(self, amount):
        self.__money -= amount

    def get_assets(self):
        print(f"이름: {self.__name}, 보유 현금: ${self.__money}")
        self.get_accounts()