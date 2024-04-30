a = int(input("Enter a number: "))


if (a == 0):
    print(f"{a} is not a power of 2")

elif (a & (a-1) == 0):
    print(f"{a} is a power of 2")

else:
    print(f"{a} is not a power of 2")
