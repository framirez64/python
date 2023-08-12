class account():
    """Class containing functions for determining account balance"""
    def __init__(self,name: str): 
        """
        Method for initializing objects for name and balance.
        :param name: Peron's name.
        
        """
        self._account_name=name
        self._account_balance=0 #Initial Account Balance

    def deposit(self,amount: int):
        """
        Method for depositing money.
        :param amount: Person's depositing amount
        :return: True if the deposit was successful, False otherwise.
        """
        if amount>0:
            self._account_balance=self._account_balance+amount #Adds deposit to account balance
            return True #If amount is more than zero, return True
        else:
            return False #If deposit is negative or less than 0, return False
        
    def withdraw(self,amount: int):
        """
        Method for withdrawing money
        :param amount: Person's withdrawing amount
        :return: True if the deposit was successful, False otherwise.
        """
        if amount >0:
            if amount <=self._account_balance: #Withdrawl ammount cannot be negative
                self._account_balance=self._account_balance-amount #Withdraws amount from account balance
                return True  #Withdrawed amount is feasible
            else:
                return False #If withdrawing amount is more than amount in account
        else:
            return False #If amount is less than zero or negative

    def get_balance(self):
        """
        Method for returning the amount in the account balance
        
        """
        return self._account_balance
    
    def get_name(self):
        """
        Method for returning the person's name
        """
        return self._account_name
