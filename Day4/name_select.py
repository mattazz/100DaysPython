import random

names = "Sarah, Mike, Ramon, Matthew, Adi, Aaron"
# .split splits a string into a list using the delimiter
names_list = names.split(",")
print(names_list)

# Select random
pick = random.randrange(0, len(names_list))
result = names_list[pick]
print(f"The person who is paying for dinner is {result}!")
