# Day 4 exercise


# x-axis  A    B    C
line1 = [" ", " ", " "]  # 1
line2 = [" ", " ", " "]  # 2
line3 = [" ", " ", " "]  # 3

###                      y-axis

map = [line1, line2, line3]
user_x = 1
user_cell = {"x": 1, "y": 1}


def print_map():
    global map  # declare map as global
    match user_cell["x"]:
        case "A":
            user_cell["x"] = 0
        case "B":
            user_cell["x"] = 1
        case "C":
            user_cell["x"] = 2

    map = [line1[:], line2[:], line3[:]]  # resets the map before new X

    map[user_cell["y"]][user_cell["x"]] = "X"
    for i in map:
        print(i)


def move():
    move = input("Where do yo want to go: ")  # up down left right
    match move:
        case "up":
            user_cell["y"] -= 1
        case "down":
            user_cell["y"] += 1
        case "left":
            user_cell["x"] -= 1
        case "right":
            user_cell["x"] += 1

    if user_cell["y"] < 0:
        user_cell["y"] = 2
    elif user_cell["y"] > 2:
        user_cell["y"] = 0

    if user_cell["x"] < 0:
        user_cell["x"] = 2
    elif user_cell["x"] > 2:
        user_cell["x"] = 0

    print(user_cell)


def main():
    print_map()  # Show where you are
    move()


while True:
    main()
