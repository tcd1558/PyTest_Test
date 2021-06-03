import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_CanCalcTotal(checkout):
    checkout.addItem("a")
    assert checkout.calcTotal() == 1

def test_CanCalcTotal2Items(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calcTotal() == 3

def test_CanAddDiscount(checkout):
    checkout.addDiscount("a", 3, 2) # item, count, discounted price

# @pytest.mark.skip
def test_CanApplyDiscount(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calcTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
            checkout.addItem('c')


# Can Create an instance of the Checkout class
# Can add an item price
# Can add an item
# Can calculate the current total
# Can add multiple items and get correct tota;
# Can add discount rules
# Can apply discount rules to the total
# Exceotion is thrwon for item added without a orice

