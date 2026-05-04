print("-- COMPOUNT INTEREST CALC --")
print("----------------------------\n")
print("Hello and welcome to the compound interest calculator!\n")
print("Calculate both your future amount and its compound interest in seconds!\n")
print("Heads up: Here are the available compound frequency (n) numbers, and here's what they mean:\n")
print("n=1 (Annually)\nn=2 (Semi-Anually)\nn=4 (Quarterly)\nn=6 (Bi-monthly)\nn=12 (Monthly)\nn=26 (Bi-weekly)\nn=52 (Weekly)\nn=365 (Daily)")

def ci_calc():
    global p, r, n, t

    while True:
        print("----------------------------\n")
        try:
            p = float(input("Enter the amount you started with: "))
            r = float(input("Enter your annual interest rate: "))
            r = r / 100
            n = float(input("Enter compound frequency (Based off given): "))
            t = float(input("Enter the amount of time (in years) that the money is saved, invested, or borrowed: "))
            if p >= 0 and r >= 0 and n >= 0 and t >= 0:
                break
            else:
                print("Negatives are invalid, especially for your principal amount and interest rate.")
                continue
        except ValueError:
            print("Inputs cannot be other than digits.")
            continue

ci_calc()

while True:
    a = p * pow((1 + (r/n)), (n*t))
    print(f"You future amount + compound interest is ${a:.2f}.")
    ci_inq = input("Do you want to know your compound interest only? (y/n): ")
    if ci_inq.lower() == "y":
        print(f"Your compound interest is ${(a - p):.2f}")
    elif ci_inq.lower() == "n":
        print("That's okay. It's better to do so, though.")

    recalc = input("Would you like to perform another calculation? (y/n): ")

    if recalc.lower() == "y":
        ci_calc()
    elif recalc.lower() == "n":
        print("Thank you for using the ci calculator!")
        break
    else:
        print("Invalid. Please enter either a 'y' or 'n'.")