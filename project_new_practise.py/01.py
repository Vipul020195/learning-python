import random

computer = random.choice ([-1, 0, 1])
youstr = input("enter your choice : ")
youdict = {"s": 1, "w": 0, "g": -1}
reversedict = {1 : "snake", 0 : "water", -1 : "gun"}

you = youdict[youstr]

print(F"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if (you == computer):
    print("draw")

else:
    if ((you == -1 and computer == 0 ) or (you == 0 and computer == 1) or (you == 1 and computer == -1)):
        print("youwin")

    else:
        print("computerwin")

print("game over")

print("thank you for playing")

print("please play again")