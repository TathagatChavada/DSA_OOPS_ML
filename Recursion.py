def factorial(val):
    if (val < 2):
        return 1
    
    return (val * factorial(val-1))

num = int(input("Ener a number to calculate its factorial: "))
print(f"Factorial of {num} is {factorial(num)}")