# Weight converter

print("--- WEIGHT CONVERTER ---\n")
print("--------------------------")
print("Welcome to the weight converter!\n")

decimal_places = 2

while True:
    try:
        weight = float(input("Enter any weight to convert: "))
        if weight <= 0:
            print("Invalid input.")
            continue
        break
    except ValueError:
        print("Invalid input.")

def conversion():
    from_unit = input("Which unit are you converting from? (kg, g, lb): ")

    while True:
        if from_unit.lower() == "kg":
            to_unit = input("Which unit are you converting to? (g, lb): ")
            if to_unit.lower() == "g":
                print(f"{weight} kg is equal to {round(weight*1000, decimal_places)} g.")
                break
            elif to_unit.lower() == "lb":
                print(f"{weight} kg is equal to {round(weight*2.20462, decimal_places)} lbs.")
                break
        elif from_unit.lower() == "g":
            to_unit = input("Which unit are you converting to? (kg, lb): ")
            if to_unit.lower() == "kg":
                print(f"{weight} g is equal to {round(weight/1000, decimal_places)} kg.")
                break
            elif to_unit.lower() == "lb":
                print(f"{weight} g is equal to {round(weight*0.00220462, decimal_places)} lbs.")
                break  
        elif from_unit.lower() == "lb":
            to_unit = input("Which unit are you converting to? (kg, g): ")
            if to_unit.lower() == "kg":
                print(f"{weight} lb is equal to {round(weight*0.453592, decimal_places)} kg.")
                break
            elif to_unit.lower() == "g":
                print(f"{weight} lb is equal to {round(weight*453.592, decimal_places)} g.")
                break
        else:
            print("Invalid input. Please choose a unit from the list.")
            from_unit = input("Which unit are you converting from? (kg, g, lb): ")
            continue 

conversion()

recon = input("Do you want to convert again? (y/n): ")

while True:        
    if recon.lower() == "n":
        print("Thank you for using the weight converter!")
        break
    elif recon.lower() == "y":
        print("-------------------------------")
        while True:
            try:
                weight = float(input("Enter any weight to convert: "))
                if weight < 0:
                    print("Invalid input.")
                    continue
                break
            except ValueError:
                print("Invalid input.")
        conversion()
        recon = input("Do you want to convert again? (y/n): ")
    else:
        print("Invalid input. Answer must be either a 'y' or 'n'.")
        recon = input("Do you want to convert again? (y/n): ")

        