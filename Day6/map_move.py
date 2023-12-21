map = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
]  # 5x5 grid


def print_map():
    global map
    for i in map:
        print(i)


print_map()

# Add player to lower left (4, 0)
loc = [4, 0]  # robot location
prev_loc = [4, 0]  # Previous location


def update_map(map):
    global prev_loc
    global loc
    # Clear prev location'
    print(f"Clearing previous loc {prev_loc}")
    map[prev_loc[0]][prev_loc[1]] = "-"
    print(f"Updating current loc {loc}")
    map[loc[0]][loc[1]] = "X"
    print(f"prev: {prev_loc}, current: {loc}")
    prev_loc = loc.copy()


update_map(map)
print_map()


# Movement Code
def move_right(spaces):
    loc[1] += spaces
    update_map(map)


def move_left(spaces):
    loc[1] -= spaces
    update_map(map)


def move_up(spaces):
    loc[0] -= spaces
    update_map(map)


def move_down(spaces):
    loc[0] += spaces
    update_map(map)


print(f"Current location: ")
update_map(map)
move_right(1)
move_up(1)
move_right(1)
move_up(1)
move_right(1)
move_up(1)

print_map()
