def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
       
    merge_sort(left_half)
    merge_sort(right_half)
    
    merge(left_half, right_half, arr)


def merge(left, right, arr):
    i = j = k = 0
    
    while  i < len(left) and j < len(right):
        if left[i] <= right[j]:

            arr[k] = left[i]
            i += 1
            
        else:
            arr[k] = right[j]
            j += 1
            
        k += 1
        
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
            

# a = [6, 5, 12, 10, 9, 1]
a = [6, 5, 12, 10]
merge_sort(a)

print(a)