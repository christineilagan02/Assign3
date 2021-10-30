# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

def getName():
    _name = input ("Name: ")
    return _name

def getAge():
    _age = input ("Age: ")
    return _age

def getAddress():
    _add = input ("Address: ")
    return _add

def display(nameF, ageF, addF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addF} .")

# steps
# 1. ask for name then save to variable
name = getName()
# 2. ask for age then save to variable
age = getAge()
# 3. ask for address then save to variable
address = getAddress()
# 4. display the details
display(name, age, address)