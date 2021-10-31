# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def buyApple(): 
    _appleAmount = int(input("How many apples do you want to buy? "))
    return _appleAmount

def buyOrange(): 
    _orangeAmount = int(input("How many oranges do you want to buy? "))
    return _orangeAmount

def showApplePrice():
    _aPrice = 20
    print(f"The price of an apple is {_aPrice} pesos.")
    return _aPrice

def showOrangePrice():
    _oPrice = 25
    print(f"The price of an orange is {_oPrice} pesos.")
    return _oPrice

def totalP():
    _appleTotalP = buy_A*applePrice()
    _orangeTotalP = buy_O*orangePrice()
    _totalPrice = _appleTotalP + _orangeTotalP
    return _totalPrice

def display(totalPrice):
    print(f"The total amount is {totalPrice} pesos. ")

# steps
# 1. ask how many apples you want to buy then save to variable
buy_A = buyApple()
# 2. ask how many oranges you want to buy then save to variable
buy_O = buyOrange()
# 3. show the price of an apple then set as a variable
applePrice = showApplePrice
# 4. show the price of an orange then set as a variable
orangePrice = showOrangePrice
# 5. solve for the total price then save to variable
totalPrice = totalP()
# 6. display the total price
total = display(totalPrice)