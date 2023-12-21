sample = range(1, 101)  # 1 - 100

res = 0


def add_even(list: range):
    global res
    for i in list:
        if i % 2 == 0:
            res += i


add_even(sample)

print(f"The total is {res}")
