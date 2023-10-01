list = [15,6,13,22,3,52,2]
n = len(list)

for i in range(n):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1], list[j]
            
            print(list)

# lst  = [1,2,3,4,5]

# lst.append(20)

# lst.extend([100,200,300])

# lst.insert(2,49)

# lst.pop()

# lst.remove(2)

# lst.reverse()

# lst.sort() 
