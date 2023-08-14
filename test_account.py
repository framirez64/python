import pytest
from account import *


class TestAccount:
    def setup_method(self):
        self.a1 = Account('Francisco')
        self.a2 = Account('John')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'Francisco'
        assert self.a1.get_balance() == 0

        assert self.a2.get_name() == 'John'
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-50) is False
        assert self.a1.get_balance() == pytest.approx(0)

        assert self.a1.deposit(50) is True
        assert self.a1.get_balance() == pytest.approx(50)

        assert self.a1.deposit(0) is False
        assert self.a1.deposit() == pytest.approx(0)

    def test_withdraw(self):
        assert self.a2.withdraw(-500) is False
        assert self.a2.withdraw() == pytest.approx(0)

        assert self.a2.withdraw(0) is False
        assert self.a2.withdraw() == pytest.approx(0)

        assert self.a2.withdraw(550) is False
        assert self.a2.withdraw() == pytest.approx(0)












































