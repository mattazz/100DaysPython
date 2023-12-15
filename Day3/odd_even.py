# Odd even exercise
def check_even_odd(num: int):
    return f"{num} is an even number" if num % 2 == 0 else f"{num} is an odd number"


print(check_even_odd(13))


def vis_square(num: int):
    # line 1 build
    for i in range(num):
        if i == 0 or i == (num - 1):
            print("#" * (num + 2))
        else:
            print("#" + " " * (num) + "#")
