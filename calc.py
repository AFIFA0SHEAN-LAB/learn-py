print("--- ARITHMETIC CALCULATOR ---\n")
print("-------------------------------")
print("Welcome to the calculator!")
print("\n+\n-\nx\n/\n")

global arithmetic
arithmetic = input("Pick an arithmetic operation: ")

while True:
    while arithmetic not in ["+", "-", "x", "/"]:
        print("Invalid input. Please pick an operation from the list.")
        print("-------------------------------")
        arithmetic = input("Pick an arithmetic operation: ")

    x = float(input("Pick your first number: "))
    y = float(input("Pick your second number: "))

    if arithmetic == "+":
        print(f"The sum of both numbers is: {x+y}")
    elif arithmetic == "-":
        print(f"The difference of both numbers is: {x-y}")
    elif arithmetic == "x":
        print(f"The product of both numbers is: {x*y}")
    elif arithmetic == "/":
        print(f"The quotient of both numbers is: {x/y}")
    
    recalc = input("Do you want to perform another calculation? (y/n): ")
    
    if recalc.lower() == "n":
        print("Thank you for using the calculator!")
        break
    elif recalc.lower() == "y":
        print("-------------------------------")
        arithmetic = input("Pick an arithmetic operation: ")
    else:
        print("Invalid input. Answer must be either a 'y' or 'n'.")
        recalc = input("Do you want to perform another calculation? (y/n): ")