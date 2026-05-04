import random

global errors, tries
tries = 3
errors = 0
global n1, n2

print("-- NUMBER GUESSING GAME ---")

def rand():
    print("---------------------------")

    global n1, n2

    while True:
        try:
            n1 = int(input("Pick any first number: "))
            n2 = int(input("Pick any second number: "))
            if n1 >= n2:
                print("Second number must be greater than the first.")
                continue
            else:
                break
        except ValueError:
            print("Values must be integers. Try again.")
            continue

def pick():
    global n1, n2
    global errors, tries

    rand_num = random.randint(n1, n2)

    while True:
        try:
            choose = int(input(f"Pick a number between {n1} amd {n2}: "))
            if choose < n1 or choose > n2:
                print("The number has to be within the range.")
                continue

            if choose > rand_num:
                errors += 1
                tries -= 1
                if tries == 1:
                    print(f"Wrong! It's a lower number! {tries} try remaining.")
                else:
                    print(f"Wrong! It's a lower number! {tries} tries remaining.")
            elif choose < rand_num:
                errors += 1
                tries -= 1
                if tries == 1:
                    print(f"Wrong! It's a higher number! {tries} try remaining.")
                else:
                    print(f"Wrong! It's a higher number! {tries} tries remaining.")
            elif choose == rand_num:
                print("Correct!")
                errors = 0
                tries = 3
                break
            
            if errors == 3:
                print(f"The correct number is: {rand_num}")
                errors = 0
                tries = 3
                break
        except ValueError:
            print("Your guess must be an integer.")
            continue

rand()
pick()

while True:
    re_guess = input("Would you like to guess again? (y/n): ")
    if re_guess.lower() == "y":
        rand()
        pick()
    elif re_guess.lower() == "n":
        print("Thank you for playing our number guessing game!")
        break
    else:
        print("Invalid input. Must either be a 'y' or an 'n'.")