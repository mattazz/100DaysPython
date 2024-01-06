test = input("To encrypt: ")


def encrypt_caesar(word: str, shift: int):
    print("Encrypting...")
    arr = []  # Empty array for the cipher
    # ord converts a character to its representative index
    # chr converts the integer back to its character (after adding the shift)
    for i in word:
        arr.append(chr(ord(i) + shift))
    return "".join(arr)


def decrypt_caesar(word: str, shift: int):
    print(f"Decrypting with shift {shift}")

    arr = []

    for i in word:
        arr.append(chr(ord(i) - shift))

    return "".join(arr)


res = encrypt_caesar(test, 1)

print("Final encrypted message: ")
print(res)


print("Decrypting...")
res = decrypt_caesar(res, 1)
print(res)
