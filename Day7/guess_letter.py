import random

player_life = 3


def check_words():
    global player_life

    words_list = ["ardvark", "baboon", "camel"]
    chosen = words_list[random.randrange(0, len(words_list))]

    # Create a list from the chosen word
    blanks = ["_" for i in chosen]
    print(blanks)

    while True:
        print(f"Player life: {player_life}")
        while True:
            letter = str(input("Guess a letter: "))
            if letter == "exit":
                print("Exiting game...")
                exit()
            try:
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

        guessed_correctly = False
        for i, char in enumerate(chosen):
            if letter == char:
                print("Right")
                blanks[i] = char
                guessed_correctly = True
            else:
                print("Wrong")

        if player_life <= 0:
            print("You lose!")
            exit()

        if not guessed_correctly:
            player_life -= 1

        print(blanks)
        if "".join(blanks) == chosen:
            print(f"The word is {chosen}. You win!")
            print("You win")
            break


check_words()
