# Problem 1
# for i in range(1,6):
    
#     for j in range(1,i):
#         print("*",end = " ")
        
#     print()    


# Problem 2
# x = int(input("Enter a number (x): "))
# n = int(input("Enter value of n: "))

# s = x
# sign = 1

# for i in range(2,n+1):
    
#     fact = 1
    
#     for j in range(1,i+1):
#         fact *= j
        
    
#     s += (sign*(x**i))/fact
#     sign *= -1
    
# print(f"The sum of first {n} terms is {s}")



# Problem 3 Number is Palindrome or not
# num  = int(input("Enter a number: "))

# wnum = num
# rev = 0

# while (wnum > 0):
#     digit = wnum % 10
#     rev = rev*10 + digit
#     wnum //= 10
    
# if  (num == rev):
#     print(f"{num} is a Palindrome number")
    
# else:
#     print(f"{num} is not a Palindrome number")
    
    

# Problem 4 Armstrong Number
# number = int(input("Enter a number: "))
# sum = 0
# temp = number

# while (temp > 0):
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
    
# if (number == sum):
#     print(f"{number} is a Armstrong Number")
    
# else: 
#     print(f"{number} is not a Armstrong Number")
    


# Problem 5 Fibonacci Series

# terms = int(input("How many terms you want in fibbonacci series? "))

# first = 0
# second = 1

# print(f"Fibonacci series is:\n {first}, {second}", end = ', ')

# for i in range(2,terms):
    
#     next = first + second
#     print(next, end = ', ')
    
#     first = second
#     second = next



# Problem 6 Contains Duplicate
# nums = [1,2,3,1]

# hashset = set()

# for i in nums:
#     if i in hashset:
#         print("True")
        
#     hashset.add(i)
    
# print("False")

