array = [3, 4, 5, 6, 7, 8, 9]
x = 4

low = 0
high = len(array)- 1
found = False

while low <= high:
    mid = low + (low + high)//2

    if (array[mid] == x):
        print(f"Element found in the Array at {mid} index position.")
        found = True
        break

    elif (array[mid] < x):
        low = mid + 1

    else:
        high = mid - 1

if (found == False):
    print("Element do not exist in the Array")