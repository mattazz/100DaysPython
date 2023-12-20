# Rock paper scissors game
import random
import time

# Rock > Scissors
# Scissors > Paper
# Paper > Rock

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

play = {"rock": "rock", "paper": "paper", "scissors": "scissors"}
art = {
    "rock_art": rock_art,
    "paper_art": paper_art,
    "scissors_art": scissors_art,
}


def main():
    while True:
        user_choice = input("What do you choose? ['rock', 'paper', 'scissors']: ")
        if user_choice.lower() in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid selection")
            continue

    print("You chose: ")
    match user_choice:
        case "rock":
            print(rock_art)
        case "paper":
            print(paper_art)
        case "scissors":
            print(scissors_art)

    # Computer turn
    think_load(3)
    ai_final_pick = ai_pick()

    # Compare

    if user_choice == ai_final_pick:
        print("Draw!")
    elif user_choice == "rock" and ai_final_pick == "paper":
        print("AI Wins!")
    elif user_choice == "rock" and ai_final_pick == "scissors":
        print("You Win!")
    elif user_choice == "paper" and ai_final_pick == "scissors":
        print("AI Wins!")
    elif user_choice == "paper" and ai_final_pick == "rock":
        print("You win!")
    elif user_choice == "scissors" and ai_final_pick == "rock":
        print("AI Wins!")
    elif user_choice == "scissors" and ai_final_pick == "paper":
        print("You win!")
    else:
        print("DIDNT CATCH THAT!")

    exit()


def think_load(num: int):
    thinking_phrases = [
        "AI is thinking hard...",
        "AI is preparing his ultimate move",
        "The AI looks at you...",
    ]

    for i in range(num):
        print(thinking_phrases[random.randrange(0, len(thinking_phrases))])
        time.sleep(0.5)


def ai_pick() -> str:
    choice = ["rock_art", "paper_art", "scissors_art"]
    ai_pick = random.randrange(0, len(choice))
    print(f"Computer chooses {ai_pick}")

    print(art[choice[ai_pick]])

    ai_final_pick = None
    match ai_pick:
        case 0:
            ai_final_pick = "rock"
        case 1:
            ai_final_pick = "paper"
        case 2:
            ai_final_pick = "scissors"

    return ai_final_pick


main()
