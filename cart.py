# Shopping cart

print("-- SHOPPING CART --")
print("-------------------\n")

cart = {}

while True:
    item = input("Enter an item (Type in q to quit): ")
    if item.lower() == "q":
        break
    if not item.isalpha():
        print("Invalid item name. Must only contain letters")
        continue

    while True:
        try: 
            price = float(input("Enter the price for the item: "))
            if float(price):
                break
            else:
                print("Invalid. Price must be a number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a price.")
            continue


    cart[item] = price

print("\n-- YOUR FINAL CART --")
for items, prices in cart.items():
    print(f"{items}: {prices}")

total = sum(cart.values())

print(f"Your total is ${total}")