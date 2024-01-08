import os

print("Welcome to the secret auction program")

bid_list = {}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def bid():
    name = input("What is your name: ")
    while True:
        try:
            bidders = input("Are there any other bidders [yes / no]: ")
            if bidders.lower() in ["yes", "no"]:
                break
        except:
            continue

    if bidders.lower() == "yes":
        while True:
            try:
                price = int(input("What is your bid: "))
                break
            except ValueError:
                print("Not a valid price.")
                continue

        bid_list[name] = price

        clear_screen()
        bid()
    else:
        while True:
            try:
                price = int(input("What is your bid: "))
                break
            except ValueError:
                print("Not a valid price.")
                continue

        bid_list[name] = price

        print(bid_list)
        check_winner(bid_list)
        exit()


def check_winner(bidder_list: dict):
    winner_name = ""
    winner_price = 0
    for k, v in bidder_list.items():
        if v > winner_price:
            winner_name = k
            winner_price = v

    print(f"The winner is {winner_name} with a bid of ${winner_price}")


bid()
