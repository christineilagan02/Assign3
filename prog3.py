# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def aMoney():
    _money = int(input("How much money do you have? "))
    return _money

def priceA():
    _pA = int(input("How much is an apple? "))
    return _pA

def totalA():
    _tA = amountMoney // priceApple
    return _tA

def sChange():
    _change = amountMoney % priceApple
    return _change

def display(totalApple, change):
    print(f"You can buy {totalApple} apples and your change is {change} pesos.")

# steps
# 1. ask for the amount of money you have then save as variable
amountMoney = aMoney()
# 2. ask for the price of an apple then save as variable
priceApple = priceA()
# 3. solve for the total amount of apples you can buy then save as variable 
totalApple = totalA()
# 4. solve for the change then save as variable
change = sChange()
# 5. display the total number of apples and the change
display(totalApple, change)