class account():
    def __init__(self,name):
        self._account_name=name
        self._account_balance=0

    def deposit(self,amount):
        if amount>0:
            self._account_balance=self._account_balance+amount
            return True
        else:
            return False
        
    def withdraw(self,amount):
        if amount >0:
            if amount <=self._account_balance:
                self._account_balance=self._account_balance-amount
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):
        return self._account_balance
    def get_name(self):
        return self._account_name
