import random
print("This is my first python project :)")

userInt = input("Choose one of the options:\n1-ROCK\n2-PAPER\n3-SCISSORS\n0-EXIT\n")
choice = int(userInt)
user = 0
pc = 0
# print(choice)
pcInt = random.randint(1, 3)

# print(pcInt)
while choice != 0:
    if pcInt == 1 and choice == 3:
        print("PS is rock, You are scissors. Lose :(")
        pc += 1
    elif pcInt == 1 and choice == 2:
        print("PS is rock, You are paper. Win :)")
        user += 1
    elif pcInt == 1 and choice == 1:
        print("PS is rock, You are rock. Draw ")
    elif pcInt == 2 and choice == 2:
        print("PS is paper, You are paper. Draw :)")
    elif pcInt == 2 and choice == 1:
        print("PS is paper, You are rock. Lose :( ")
        pc += 1
    elif pcInt == 2 and choice == 3:
        print("PS is paper, You are scissors. Win :)")
        user += 1
    elif pcInt == 3 and choice == 1:
        print("PS is scissors, You are rock. Win :) ")
        user += 1
    elif pcInt == 3 and choice == 2:
        print("PS is scissors, You are paper.Lose :( ")
        pc += 1
    elif pcInt == 3 and choice == 3:
        print("PS is scissors, You are scissors. Draw :)")
    print("Skor: PC " + str(pc) + "-" + str(user) + " Oyuncu")
    userInt = input("Birini seçiniz:\n1-Taş\n2-Kağıt\n3-Makas\n0-Çıkış\n")
    choice = int(userInt)
    pcInt = random.randint(1, 3)

print(("GAME OVER").center(20))
print("Skor: PC " + str(pc) + "-" + str(user) + " Player")
if(user < pc):
    print(("YOU LOST").center(20))
elif(user == pc):
    print(("DRAW").center(20))
else:
    print(("YOU WON").center(20))
