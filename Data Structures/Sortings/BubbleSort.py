lst = [15, 6, 13, 22, 3, 52, 2]
n = len(lst)


for i in range(n):
    
    swapped = False
    
    for j in range(0,n-i-1):
        
        if lst[j] > lst[j+1]:
            
            lst[j], lst[j+1] = lst[j+1], lst[j]
            swapped = True
            
    if not swapped:
        break
    
print(lst)