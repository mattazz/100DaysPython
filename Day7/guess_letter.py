import random

while True:
    try:
        letter = str(input("Guess a letter: "))
        if len(letter) > 1:
            print("Too many letters")
            continue
        elif letter.isdigit():
            print("Cannot be a number")
            continue
        else:
            break
    except:
        print("Invalid input")

print(f"You chose: {letter}")


def check_words(letter):
    words_list = ["ardvark", "baboon", "camel"]
    chosen = words_list[random.randrange(0, len(words_list))]

    for char in chosen:
        if letter == char:
            print("Right")
        else:
            print("Wrong")


check_words(letter)
