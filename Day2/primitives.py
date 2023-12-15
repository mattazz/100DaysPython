# String Indexing
string = "Hello World"
print(f"Hello world can be dissected by indexing the strings as separate characters")
for i, v in enumerate(string):
    print(f"{i}: {v}")


# String > int parsing exercise
print("String exercise: ")


def add_strings(str: str):
    return int(str[0]) + int(str[1])


print(add_strings("39"))
