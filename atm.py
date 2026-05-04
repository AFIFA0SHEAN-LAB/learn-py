# SMART ATM SYSTEM 

# Account Details
AccPIN = 8920
Balance = 1000

# ATM PIN Entry
errors = 0
tries = 3

def atm():
    global Balance
    while True:
        try:
            print("---------------\n")
            print("Check Balance\nDeposit\nWithdraw\nExit\n")
            options = input("Pick your next option on the menu: ")
            if options.lower() == "balance":
                print(f"Your balance is: ${Balance}")
                other_tran = input("Would you like to complete another transaction? (y/n): ")
                if other_tran.lower() == "y":
                    continue
                elif other_tran.lower() == "n":
                    print("Thank you for visiting our ATM!")
                    break
                else:
                    print("Invalid. Please respond with a 'y' or 'n'.")
            elif options.lower() == "deposit":
                deposit = float(input("Enter deposit amount: "))
                if deposit > 0:
                    Balance += deposit
                    print("Deposited! Your balance is now $", Balance)
                    other_tran = input("Would you like to complete another transaction? (y/n): ")
                    if other_tran.lower() == "y":
                        continue
                    elif other_tran.lower() == "n":
                        print("Thank you for visiting our ATM!")
                        break
                    else:
                        print("Invalid. Please respond with a 'y' or 'n'.")
                else:
                    print(f"Cannot deposit negative or zero currency.")
                    continue
            elif options.lower() == "withdraw":
                while True:
                    withdraw = float(input("Enter withdrawal amount: "))
                    if withdraw > Balance:
                        print("Cannot withdraw amount greater than balance.")
                        continue
                    elif withdraw > 0:
                        withdraw_ratio = (withdraw/Balance)*100
                        if withdraw_ratio >= 70:
                            print(f"You're withdrawal is {round(withdraw_ratio, 2)}% of your whole balance.")
                            conf_withdrawal = input("Are you sure? (y/n): ")
                            if conf_withdrawal.lower() == "y":
                                Balance -= withdraw
                                print("Withdrawn! Your balance is now $", Balance)
                            elif conf_withdrawal.lower() == "n":
                                print("Withdrawal cancelled.")
                                break
                        other_tran = input("Would you like to complete another transaction? (y/n): ")
                        if other_tran.lower() == "y":
                            break
                        elif other_tran.lower() == "n":
                            print("Thank you for visiting our ATM!")
                            break
                        else:
                            print("Invalid. Please respond with a 'y' or 'n'.")
                    else:
                        print("Cannot withdraw zero or negative currency.")
                        continue
            elif options.lower() == "exit":
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == "y":
                    print("Thank you for using our ATM!")
                    break
                elif confirm.lower() == "n":
                    continue
        except ValueError:
            print("Invalid. Please choose one of the four choices.")
            continue

while True:
    try:
        Enter_PIN = int(input("Please enter your 4-digit PIN: "))
        if Enter_PIN == AccPIN:
            print("Access Granted!")
            atm()
            break
        else:
            errors += 1
            tries -= 1
            print(f"Wrong. Please enter the correct PIN. {tries} attempts remaining.")
            if errors == 3:
                print("Invalidated 3 times. Exiting ATM...")
                break

    except ValueError:
            errors += 1
            tries -= 1
            print(f"Invalid. Please enter a PIN. {tries} attempts remaining.")
            if errors == 3:
                print("Invalidated 3 times. Exiting ATM...")
                break
            else:
                atm()