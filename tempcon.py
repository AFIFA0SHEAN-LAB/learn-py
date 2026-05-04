print("--- TEMPERATURE CONVERTER ---")
print("-----------------------------")

while True:
    try:
        temp = float(input("Enter your temperature to convert (Must be a number): "))
        break
    except ValueError:
        print("Invalid input. Please enter a number")
        continue

def temp_conversion():
    while True:
        temp_from = input("Which temperature unit would you like to convert from? (C, K, F): ")

        if temp_from.lower() == "c":
            temp_to = input("Which temperature unit would you like to convert to? (F, K): ")
            if temp_to.lower() == "f":
                print(f"{temp} degrees C = {(temp*(9/5)) + 32} degrees F")
                break
            elif temp_to.lower() == "k":
                print(f"{temp} degrees C = {temp + 273.15}K")
                break
            else:
                print("Invalid input. Please choose one of the two listed to convert.")
        elif temp_from.lower() == "k":
            temp_to = input("Which temperature unit would you like to convert to? (C, F): ")
            if temp_to.lower() == "c":
                print(f"{temp}K = {temp - 273.15} degrees C")
                break
            elif temp_to.lower() == "f":
                print(f"{temp}K = {((temp - 273.15)*(9/5)) + 32} degrees F")
                break
            else:
                print("Invalid input. Please choose one of the two listed to convert.")
        elif temp_from.lower() == "f":
            temp_to = input("Which temperature unit would you like to convert to? (C, K): ")
            if temp_to.lower() == "c":
                print(f"{temp} degrees F = {(temp - 32)*(5/9)} degrees C")
                break
            elif temp_to.lower() == "k":
                print(f"{temp} degrees F = {((temp - 32)*(5/9)) + 273.15}K")
                break
            else:
                print("Invalid input. Please choose one of the two listed to convert.")
        else:
            print("Invalid input. Please pick a given temperature unit (C, K, F).")
            continue
temp_conversion()

recon = input("Would you like to convert again? (y/n): ")

while True:
    if recon.lower() == "n":
        print("Thank you for using our temp converter!")
        break
    elif recon.lower() == "y":
        print("-----------------------------")
        while True:
            try:
                temp = float(input("Enter your temperature to convert (Must be a number): "))
                break
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
        temp_conversion()
        recon = input("Would you like to convert again? (y/n): ")
    else:
        print("Invalid. Please enter either a 'y' or 'n'.")
        recon = input("Would you like to convert again? (y/n): ")