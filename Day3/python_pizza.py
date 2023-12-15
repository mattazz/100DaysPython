# size = input() S M L
# add_pepperoni = input() y/n
# extra_cheese = input() y/n


def order_pizza():
    sizes = ["S", "M", "L"]
    cost = 0
    while True:
        size = input("Size: (S, M, or L): ")
        if len(size) > 1:
            print(f"Please type either S, M, or L for the size")
            continue
        elif size.upper() in sizes:
            print(f"You chose the size {size}")
            break
        else:
            print(f"Please put in a valid response.")

    while True:
        pepperoni = input("Do you want pepperoni on it (y/n): ")
        if pepperoni.lower() in ["y", "n"]:
            if pepperoni.lower() == "n":
                print("You did not want any pepperoni on it.")
            else:
                print("You wanted pepperoni on it.")
            break
        else:
            print("Please input a valid response.")
            continue

    while True:
        cheese = input("Do you extra cheese on it (y/n): ")
        if pepperoni.lower() in ["y", "n"]:
            if pepperoni.lower() == "n":
                print("You did not want any extra cheese on it.")
            else:
                print("You wanted extra cheese on it.")
            break
        else:
            print("Please input a valid response.")
            continue

    # Calculate costs
    match size.upper():
        case "S":
            cost += 15
            if pepperoni.upper() == "Y":
                cost += 2
            if cheese.upper() == "Y":
                cost += 1
        case "M":
            cost += 20
            if pepperoni.upper() == "Y":
                cost += 3
            if cheese.upper() == "Y":
                cost += 1
        case "L":
            cost += 25
            if pepperoni.upper() == "Y":
                cost += 3
            if cheese.upper() == "Y":
                cost += 1

    print(f"Total cost of the pizza: ${cost}")


order_pizza()
