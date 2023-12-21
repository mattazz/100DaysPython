import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def pass_gen() -> str:
    letter_len = len(letters)
    sym_len = len(symbols)
    num_len = len(numbers)

    res = []

    while True:
        try:
            chars = int(input("How many letters would you like for your password: "))
            sym = int(input("How many symbols?: "))
            num = int(input("How many numbers?: "))
            break

        except ValueError:
            print("Enter a valid number. Restarting questions.")
            continue

    # Generate password

    # Letters
    for i in range(0, chars + 1):
        rand = random.randrange(0, letter_len)
        res.append(letters[rand])

    for i in range(0, sym + 1):
        rand = random.randrange(0, sym_len)
        res.append(symbols[rand])

    for i in range(0, num + 1):
        rand = random.randrange(0, num_len)
        res.append(numbers[rand])

    random.shuffle(res)  # Shuffles the order
    res = "".join(res)  # list -> String
    return res


user_pass = pass_gen()
print(f"Password is: {user_pass}")
