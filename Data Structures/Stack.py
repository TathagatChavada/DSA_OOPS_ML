class create_stack:
    
    def __init__(self):
        self.stk = []
        self.top = None


    def isEmpty(self, stk):
        if self.stk == []:
            return True
        
        else:
            return False


    def Push(self, item):
        self.stk.append(item)
        self.top = len(self.stk) - 1
        

    def Pop(self):
        if self.isEmpty(self.stk):
            print("Underflow")
        
        else:
            item = self.stk.pop()
            if (len(self.stk) == 0):
                self.top = None
                
            else:
                self.top = len(self.stk) - 1
                
            print("Popped item is: ", item)
        
        
    def Peek(self):
        if self.isEmpty(self.stk):
            print("Underflow")
        
        else:
            self.top = len(self.stk) - 1
            print("\n")
            print("Topmost item is: ", self.stk[self.top])
        

    def Display(self):
        if self.isEmpty(self.stk):
            print("Stack is Empty")   
        
        else:
            self.top = len(self.stk) - 1
            
            print(self.stk[self.top],"<--- Top")
            for i in range(self.top-1,-1,-1):
                print(self.stk[i])
        
stack1 = create_stack()

stack1.Push(1)
stack1.Push(2)
stack1.Push(3)
stack1.Push(4)
stack1.Push(5)
stack1.Push(6)

stack1.Display()

stack1.Peek()
stack1.Pop()
stack1.Display()