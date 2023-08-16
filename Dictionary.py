# M = {}

# n = int(input("Enter a number: "))

# for i in range(n):
#     rollNo = int(input('Enter your Roll No: '))
#     marks = int(input('Enter your Marks: '))
#     M[rollNo] = marks
    
# print(M)

dict = {1:'one', 2:'two', 3:'three'}

# To get the values of the given key
print(dict.get(1))

# To get all items (key:value) pairs of the dictionary
l = dict.items()
for i in l:
    print(i)

# To get all the keys of the dictionary
print(dict.keys())

# To get all the values of the dictionary
print(dict.values())