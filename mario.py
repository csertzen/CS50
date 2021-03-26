while(True):
    marioHeight = input("How tall is Mario: ")
    marioHeightInt = int(marioHeight)

    if marioHeightInt >= 1 and marioHeightInt <= 8:
        print(marioHeightInt, "Valid", end='')
        for i in range(marioHeightInt + 1):
            print(" "*(marioHeightInt-i),"#"*i)
    else:
        print(marioHeightInt, "Invalid")