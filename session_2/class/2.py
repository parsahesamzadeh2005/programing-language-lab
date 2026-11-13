
# play gta vi

# Requirements:
# age >= 18
# if age < 18, must have parent permission
# must have a gaming console
# must have 80 or 100 dollars to buy the game

age = int(input("Enter you age : "))

if age >= 18:
    allowed = True
else:
    premission = int(input("your age is below 18 do you have premission of parentingsionfullyness? if yes input 1: "))
    
    if premission == 1:
        allowed = True
    else:
        allowed = False

if allowed:
    console = int(input("Do you have a gaming console? if yes input 1: "))

    if console == 1:
        money = int(input("Do you have 80 or 100 dollars to buy the game? if yes input 1: "))

        if money == 1:
            print("youre allowed")
        else:
            print("your are irani or poor lil vro💀😭")
    else:
        print("get a job !!!")

else:
    print("your not allowed lil vro💀😭")
