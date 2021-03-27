while(True):
    quarter = 5
    dime = 0
    nickel = 5
    penny = 1
    coins = 0
    changeInput = input("Change owed: ")
    usrInput = changeInput.strip("$")
    floatInput = float(usrInput)
    if floatInput > 0:
        coins = floatInput * 100
        cents = 100 - coins
        
        