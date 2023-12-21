sample = range(1, 101)  # 1 - 100


def fizz_buzz():
    global sample
    for i in sample:
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - Fizzbuzz!")
        elif i % 3 == 0:
            print(f"{i} - Fizz")
        elif i % 5 == 0:
            print(f"{i} - Buzz")
        else:
            print(f"{i}")


fizz_buzz()
