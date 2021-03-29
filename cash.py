while(True):
    quarter = 25
    dime = 0
    nickel = 5
    penny = 1
    coins = 0
    changeInput = input("Change owed: ")
    usrInput = changeInput.strip("$")
    floatInput = float(usrInput)
    if floatInput > 0.00:
        cents = int(floatInput * 100)
        while(cents >= 25):
            cents -= 25
            print("Cents: ", cents)
        