while(True):
    marioHeight = input("How tall is Mario: ")
    marioHeightInt = int(marioHeight)

    if marioHeightInt >= 1 and marioHeightInt <= 8:
        print("Valid height")
    else:
        print("Invalid height")