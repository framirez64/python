class Account():
    """Class containing functions for determining account balance"""
    def __init__(self,name: str) -> None: 
        """
        Method for initializing objects for name and balance.
        :param name: Peron's name.
        
        """
        self.__account_name=name
        self.__account_balance=0 #Initial Account Balance

    def deposit(self,amount: float) -> bool:
        """
        Method for depositing money.
        :param amount: Person's depositing amount
        :return: True if the deposit was successful, False otherwise.
        """
        if amount>0:
            self.__account_balance=self.__account_balance+amount #Adds deposit to account balance
            return True #If amount is more than zero, return True
        else:
            return False #If deposit is negative or less than 0, return False
        
    def withdraw(self,amount: float) -> bool:
        """
        Method for withdrawing money
        :param amount: Person's withdrawing amount
        :return: True if the deposit was successful, False otherwise.
        """
        if amount >0:
            if amount <=self.__account_balance: #Withdrawl ammount cannot be negative
                self.__account_balance=self.__account_balance-amount #Withdraws amount from account balance
                return True  #Withdrawed amount is feasible
            else:
                return False #If withdrawing amount is more than amount in account
        else:
            return False #If amount is less than zero or negative

    def get_balance(self) -> float:
        """
        Method for returning the amount in the account balance
        
        """
        return self.__account_balance
    
    def get_name(self) -> str:
        """
        Method for returning the person's name
        """
        return self.__account_name
