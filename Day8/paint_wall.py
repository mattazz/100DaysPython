# 1 can of paint can cover 5 square meters of wall
# Calculate how many cans of paint you'll need to buy


def calculate(height, width):
    coverage = 5
    result = (height * width) / coverage
    print(result)
    result = int(round(result, 0))
    print(f"You'll need {result} cans of paint!")


while True:
    try:
        height = int(input("What is the wall height: "))
        width = int(input("What is the wall width? "))
        break
    except ValueError:
        print("Must have a valid height and width")
        continue

calculate(height, width)
