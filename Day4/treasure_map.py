# Day 4 exercise

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]


def print_map(map: list):
    for i in map:
        print(i)


print_map(map)

user = input("Where do you want to hide the map: ")

col = user[1].upper()  # A, B, C
row = user[0]  # 1, 2, 3 as string

list_row = int(row) - 1
list_col = None

match col:
    case "A":
        list_col = 0
    case "B":
        list_col = 1
    case "C":
        list_col = 2

map[int(list_row)][list_col] = "X"

print_map(map)
