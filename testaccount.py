import pytest
from account import account

def test__init__():
    name = account('Francisco')
    assert name.get_name() == 'Francisco'
    assert name.get_balance() == 0

def test_deposit():
    name = account('Francisco')
    name.deposit(40)
    assert name.get_balance() == pytest.approx(40)
    name.deposit(-2)
    assert name.deposit(-2) is False
    assert name.get_balance() == pytest.approx(40)
    name.deposit(0)
    assert name.deposit(0) is False
    assert name.get_balance() == pytest.approx(40)

def test_withdrawl():
    name = account('Francisco')
    name.deposit(50)
    name.withdraw(30)
    assert name.get_balance() == 20
    name.withdraw(30)
    assert name.withdraw(30) is False
    assert name.get_balance() == pytest.approx(20)
    name.withdraw(0)
    assert name.withdraw(0) is False
    assert name.get_balance() == pytest.approx(20)
    name.withdraw(-400)
    assert name.withdraw(-400) is False
    assert name.get_balance() == pytest.approx(20)
    
    






