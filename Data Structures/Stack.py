def isEmpty(stk):
    if stk == []:
        return True
    
    else:
        return False


def Push(stk,item):
    stk.append(item)
    top = len(stk) - 1
    

def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    
    else:
        item = stk.pop()
        if (len(stk) == 0):
            top = None
            
        else:
            top = len(stk) - 1
            
        return item
    
    
def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    
    else:
        top = len(stk) - 1
        return stk[top]
    

def Display(stk):
    if isEmpty(stk):
        return "Stack is Empty"   
    
    else:
        top = len(stk) - 1
        
        print(stk[top],"<--- Top")
        for i in range(top-1,-1,-1):
            print(stk[i])
    
    
Stack = []
top = None

while True:
    print()
    print("Stack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")
    
    ch = int(input("Enter your choice(1-5): "))
    
    if ch == 1:
        print()
        item = int(input("Enter item: "))
        Push(Stack,item)
        
    elif ch == 2:
        item = Pop(Stack)  
        if item == "Undeflow":
            print()
            print("Underflow! Stack is Empty")
            
        else:
            print()
            print(f"Popped item is {item}")
            
    elif ch == 3:
        item = Peek(Stack)  
        if item == "Undeflow":
            print()
            print("Underflow! Stack is Empty")
            
        else:
            print()
            print(f"Topmost item is {item}")
            
            
    elif ch == 4:
        print()
        Display(Stack)
        
    elif ch == 5:
        break
    
    else:
        print("Invalid Choice!")