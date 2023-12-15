print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
'''
)

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

print("\n")

print("You arrive on the island and jump out of your boat.")
print("You walk for a few minutes into the dense jungle and arrive a fork in the road.")
print("Both roads seem to be the same... ")
print("\n")

while True:
    direction = input("Would you like to go left or right: ")
    direction = direction.lower()
    if direction in ["left", "right"]:
        if direction == "left":
            break
        else:
            print(
                "You choose the right road and walk a few minutes. You start hearing deafening howls from the trees..."
            )
            print("A group of baboons with glowing red eyes start swarming you!")
            print("Game over!")
            exit()
    else:
        print("Please enter a valid action")
        continue
print("\n")
print(
    "You take the left road which seems to be the right one...you hear roars on the road opposite to you."
)
print("When you get out of the jungle you enter a clearing with an expansive lake.")
print(
    "There seems to be something at the end of the lake but you can't quite make out what it is."
)
print(
    "You can try swimming the lake and get to the object...or wait and see what happens."
)
print("\n")

while True:
    direction = input("Do you want to swim or wait: ")
    direction = direction.lower()
    if direction in ["swim", "wait"]:
        if direction == "swim":
            print("You bravely start swimming across the lake!")
            print(
                "It seems like forever but the end of the lake doesn't seem to be getting nearer."
            )
            print("You feel your muscles cramp and slowly give in to the fatigue.")
            print("You drown! Game over!")
            exit()
        else:
            break
    else:
        print("Please print a valid response")

print("\n")

print("You wait and see what happens...")
print(
    "Suddenly, the lake starts draining! You watch in amazement as the lake eventually becomes barren and dry."
)
print(
    "You just walk towards the object and after a few hours arrive in front of the mysterious object. A door."
)
print(
    "Actually...there are three doors! One is red, one is yellow, and the last one is blue."
)
print("\n")

while True:
    direction = input("Which door do you want to open [red, blue, yellow]: ")
    direction = direction.lower()
    if direction in ["red", "blue", "yellow"]:
        match direction:
            case "red":
                print(
                    "You open the red door and a fountain of blood gushes through it!"
                )
                print("You see an army of bloody skeletons rushing through the door!")
                print("They start leaping towards you and rip your flesh off!")
                print("Game over!")
                exit()
            case "blue":
                print("Game over!")
                print(
                    "You open the blue door and the lake magically starts filling up with water!"
                )
                print(
                    "Acutally... it doesn't stop and continues to pour water where even the island is submerged."
                )
                print("You seem to now be swiming with no body of land nearby.")
                print("After a few hours of floating...you slowly give in...Game over!")
                exit()
            case "yellow":
                print(
                    "You open the yellow door and see the glow of a chest surrounded with gold coins and objects!"
                )
                print("You're rich!!")
                print("You win!")
                exit()
    else:
        print("Please input a valid action")
