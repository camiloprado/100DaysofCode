print("Welcome to Treasure Insland. Your mission is to find the treasure. Good Luck!")
print("You see a path.")
choice1 = str(input("Where are you want to go? Left or Right (L/R): ")).upper()
if choice1 == "LEFT" or choice1 == "L":
    print("You see a restless lake.")
    choice2 = str(input("What you want to do? Swim or Wait (S/W): ")).upper()
    if choice2 == "WAIT" or choice2 == "W":
        print("You wait for the lake to calm down. You find 3 doors.")
        choice3 = str(input("What door do you wnat to open? Red or Yellow or Blue (R/Y/B): ")).upper()
        if choice3 == "Red" or choice3 == "R":
            print("Game Over!")
        elif choice3 == "Yellow" or choice3 == "Y":
            print("You Win!")
        elif choice3 == "Blue" or choice3 == "B":
            print("Game Over!")
        else:
            print("Wrong Choice. Game Over!")
    elif choice2 == "SWIM" or choice2 == "S":
        print("Game Over!")
    else:
            print("Wrong Choice. Game Over!")
elif choice1 == "RIGHT" or choice1 == "R":
        print("Game Over!")
else:
        print("Wrong Choice. Game Over!")