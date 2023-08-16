lst = [11,55,36,42,89,100,121,56]
element = int(input("Enter a no. that you want to search: "))

for i,n in enumerate(lst):
    if n == element:
        print(f"Element {n} is at index position:",i)
        print(list(enumerate(lst)))
        break
    
else:
    print("Element is not given in the list")
    

# num = int(input("Enter a number: "))

# const = num
# rev = 0

# while (const > 0):
#     digit = const % 10
#     rev = rev*10 + digit
#     const //= 10
    
# if (num == rev):
#     print(f"{num} is a palindrome number.")
    
# else:
#     print(f"{num} is not a palindrome number.")
