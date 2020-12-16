
# import random module
import random

# import time module
import time

# asking the user if he wants a custom DICE which has the chance of getting custom number at custom percent
print(" Do you want a Normal Dice or a Dice with custom chance of getting custom number at custom percentage?")

time.sleep(0.25)
user = str.upper(input(" Enter N for Normal and C for Custom ( N / C ) \n>> "))
c = "Y"
if user == "N":
    while c == "Y":
        # pick a random number between 1 to 6 cause dice has number from 1 to 6 only
        a = random.randint(1, 7)
        if a == 1:
            print("----------")
            print("|        |")
            print("|    O   |")
            print("|        |")
            print("----------")
        elif a == 2:
            print("----------")
            print("|        |")
            print("| O    O |")
            print("|        |")
            print("----------")
        elif a == 3:
            print("----------")
            print("|    O   |")
            print("|    O   |")
            print("|    O   |")
            print("----------")
        elif a == 4:
            print("----------")
            print("| O    O |")
            print("|        |")
            print("| O    O |")
            print("----------")
        elif a == 5:
            print("----------")
            print("| O    O |")
            print("|    O   |")
            print("| O    O |")
            print("----------")
        elif a == 6:
            print("----------")
            print("| O    O |")
            print("| O    O |")
            print("| O    O |")
            print("----------")
        print("")
        # make the code below this command execute only after some seconds inputed
        time.sleep(0.75)

        # This code will only execute after the inputed seconds
        c = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
elif user == "C":
    user1 = int(input("Of which number do you want to have the higher chance? (1/ 2/ 3/ 4/ 5/ 6)\n >>"))
    pos = float(input("Your desired chance of getting that number ? \n>>"))
    chance = float(pos/100)
    if user1 == 1:
        while c == "Y":
            d = random.random()
            print(chance, " is the probability")
            if d <= chance:
                a = 1
                print("----------")
                print("|        |")
                print("|    O   |")
                print("|        |")
                print("----------")
            elif d > chance:
                a = random.randint(2, 7)
                if a == 2:
                    print("----------")
                    print("|        |")
                    print("| O    O |")
                    print("|        |")
                    print("----------")
                elif a == 3:
                    print("----------")
                    print("|    O   |")
                    print("|    O   |")
                    print("|    O   |")
                    print("----------")
                elif a == 4:
                    print("----------")
                    print("| O    O |")
                    print("|        |")
                    print("| O    O |")
                    print("----------")
                elif a == 5:
                    print("----------")
                    print("| O    O |")
                    print("|    O   |")
                    print("| O    O |")
                    print("----------")
                elif a == 6:
                    print("----------")
                    print("| O    O |")
                    print("| O    O |")
                    print("| O    O |")
                    print("----------")
                print("")
            # make the code below this command execute only after some seconds inputed
            time.sleep(0.75)
            # This code will only execute after the inputed seconds
            c = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
    elif user1 == 2:
        while c == "Y":
            d = random.random()
            print(chance, " is the probability")
            if d <= chance:
                a = 2
                print("----------")
                print("|        |")
                print("| O    O |")
                print("|        |")
                print("----------")
            elif d > chance:
                a = random.choice([1, 3, 4, 5, 6])
                if a == 1:
                    print("----------")
                    print("|        |")
                    print("|    O   |")
                    print("|        |")
                    print("----------")
                elif a == 3:
                    print("----------")
                    print("|    O   |")
                    print("|    O   |")
                    print("|    O   |")
                    print("----------")
                elif a == 4:
                    print("----------")
                    print("| O    O |")
                    print("|        |")
                    print("| O    O |")
                    print("----------")
                elif a == 5:
                    print("----------")
                    print("| O    O |")
                    print("|    O   |")
                    print("| O    O |")
                    print("----------")
                elif a == 6:
                    print("----------")
                    print("| O    O |")
                    print("| O    O |")
                    print("| O    O |")
                    print("----------")
                print("")
                # make the code below this command execute only after some seconds inputed
                time.sleep(0.75)
            # This code will only execute after the inputed seconds
            c = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
    elif user1 == 3:
        while c == "Y":
            d = random.random()
            print(chance, " is the probability")
            if d <= chance:
                a = 3
                print("----------")
                print("|    O   |")
                print("|    O   |")
                print("|    O   |")
                print("----------")
            elif d > chance:
                a = random.choice([1, 2, 4, 5, 6])
                if a == 1:
                    print("----------")
                    print("|        |")
                    print("|    O   |")
                    print("|        |")
                    print("----------")
                elif a == 2:
                    print("----------")
                    print("|        |")
                    print("| O    O |")
                    print("|        |")
                    print("----------")
                elif a == 4:
                    print("----------")
                    print("| O    O |")
                    print("|        |")
                    print("| O    O |")
                    print("----------")
                elif a == 5:
                    print("----------")
                    print("| O    O |")
                    print("|    O   |")
                    print("| O    O |")
                    print("----------")
                elif a == 6:
                    print("----------")
                    print("| O    O |")
                    print("| O    O |")
                    print("| O    O |")
                    print("----------")
                print("")
                # make the code below this command execute only after some seconds inputed
                time.sleep(0.75)
            # This code will only execute after the inputed seconds
            c = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
    elif user1 == 4:
        while c == "Y":
            d = random.random()
            print(chance, " is the probability")
            if d <= chance:
                a = 4
                print("----------")
                print("| O    O |")
                print("|        |")
                print("| O    O |")
                print("----------")

            elif d > chance:
                a = random.choice([1, 2, 3, 5, 6])
                if a == 1:
                    print("----------")
                    print("|        |")
                    print("|    O   |")
                    print("|        |")
                    print("----------")
                elif a == 2:
                    print("----------")
                    print("|        |")
                    print("| O    O |")
                    print("|        |")
                    print("----------")
                elif a == 3:
                    print("----------")
                    print("|    O   |")
                    print("|    O   |")
                    print("|    O   |")
                    print("----------")

                elif a == 5:
                    print("----------")
                    print("| O    O |")
                    print("|    O   |")
                    print("| O    O |")
                    print("----------")
                elif a == 6:
                    print("----------")
                    print("| O    O |")
                    print("| O    O |")
                    print("| O    O |")
                    print("----------")
                print("")
                # make the code below this command execute only after some seconds inputed
                time.sleep(0.75)
            # This code will only execute after the inputed seconds
            c = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
    elif user1 == 5:
        while c == "Y":
            d = random.random()
            print(chance, " is the probability")
            if d <= chance:
                a = 5
                print("----------")
                print("| O    O |")
                print("|    O   |")
                print("| O    O |")
                print("----------")
            elif d > chance:
                a = random.choice([1, 2, 3, 4, 6])

                if a == 1:
                    print("----------")
                    print("|        |")
                    print("|    O   |")
                    print("|        |")
                    print("----------")
                elif a == 2:
                    print("----------")
                    print("|        |")
                    print("| O    O |")
                    print("|        |")
                    print("----------")
                elif a == 3:
                    print("----------")
                    print("|    O   |")
                    print("|    O   |")
                    print("|    O   |")
                    print("----------")
                elif a == 4:
                    print("----------")
                    print("| O    O |")
                    print("|        |")
                    print("| O    O |")
                    print("----------")
                elif a == 6:
                    print("----------")
                    print("| O    O |")
                    print("| O    O |")
                    print("| O    O |")
                    print("----------")
                print("")
                # make the code below this command execute only after some seconds inputed
                time.sleep(0.75)
            # This code will only execute after the inputed seconds
            c = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
    elif user1 == 6:
        while c == "Y":
            d = random.random()
            print(chance, " is the probability")
            if d <= chance:
                a = 6
                print("----------")
                print("| O    O |")
                print("| O    O |")
                print("| O    O |")
                print("----------")
            elif d > chance:
                a = random.choice([1, 2, 3, 4, 5])
                if a == 1:
                    print("----------")
                    print("|        |")
                    print("|    O   |")
                    print("|        |")
                    print("----------")
                elif a == 2:
                    print("----------")
                    print("|        |")
                    print("| O    O |")
                    print("|        |")
                    print("----------")
                elif a == 3:
                    print("----------")
                    print("|    O   |")
                    print("|    O   |")
                    print("|    O   |")
                    print("----------")
                elif a == 4:
                    print("----------")
                    print("| O    O |")
                    print("|        |")
                    print("| O    O |")
                    print("----------")
                elif a == 5:
                    print("----------")
                    print("| O    O |")
                    print("|    O   |")
                    print("| O    O |")
                    print("----------")
                print("")
                # make the code below this command execute only after some seconds inputed
                time.sleep(0.75)
            # This code will only execute after the inputed seconds
            c = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
