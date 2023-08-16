lst = [9, 5, 1, 4, 3]
size = len(lst)

for i in range(1, size):
    key = lst[i]
    j = i - 1
    
    while j >=0 and key < lst[j]:
        
        lst[j + 1] = lst[j]
        j -= 1
        
    lst[j + 1] = key
    print(lst)