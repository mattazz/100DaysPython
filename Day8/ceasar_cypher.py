def encrypt_caesar(shift: int):
    word = input("Enter a message to encrypt: ")
    print("Encrypting...")
    arr = []  # Empty array for the cipher
    # ord converts a character to its representative index
    # chr converts the integer back to its character (after adding the shift)
    for i in word:
        arr.append(chr(ord(i) + shift))
    return "".join(arr)


def decrypt_caesar(shift: int):
    word = input("Enter a message to decrypt: ")
    print(f"Decrypting with shift {shift}")

    arr = []

    for i in word:
        arr.append(chr(ord(i) - shift))

    return "".join(arr)


def menu():
    items = ["Encrypt", "Decrypt", "Exit"]

    for i, v in enumerate(items):
        print(f"[{i}: {v}]")

    while True:
        try:
            user_action = int(input("Select from the menu: "))
            if user_action > len(items) or user_action < 0:
                print("Not a valid action. Out of index range.")
                input("Press enter to continue")
                continue
            else:
                break
        except:
            print("Please input a valid action.")
            input("Press enter to continue")
            continue

    match user_action:
        case 0:
            res = encrypt_caesar(1)
            print(f"Encrypted message: {res}")
            input("Press enter to continue")
        case 1:
            decrypt_caesar(1)
            res = decrypt_caesar(1)
            print(f"Decrypted message: {res}")
            input("Press enter to continue")

        case 2:
            print("Exiting program.")
            exit()


while True:
    menu()
