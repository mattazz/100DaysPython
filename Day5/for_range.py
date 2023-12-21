# Looping through range function

print(f"range(1,10) does not print the last number of the second parameter")
for i in range(1, 10):
    print(i, end=",")

print("\n")
print(f"It needs to be range(x, y+1); y += 1 to get the number end range")
for i in range(1, 11):
    print(i, end=",")
