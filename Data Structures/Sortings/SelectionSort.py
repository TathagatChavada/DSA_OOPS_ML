lst = [-2, 45, 0, 11, -9]
size = len(lst)

for step in range(size):
    
    # shifts pointer to the next element after min is placed at correct position
    min_idx = step
    
    for i in range(step + 1, size):
        
        if lst[i] < lst[min_idx]:
            min_idx = i
            
    # put min at the correct position
    lst[step], lst[min_idx] = lst[min_idx], lst[step]
    
    print(lst)