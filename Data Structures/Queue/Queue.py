class Queue:
    
    def __init__(self):
        self.queue = []
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        if self.queue == []:
            return True
        
        else:
            return False


    def Enqueue(self, item):
        self.queue.append(item)
        
        if len(self.queue) == 1:
            self.front = self.rear = 0
        
        else:
            self.rear = len(self.queue) - 1
        

    def Dequeue(self):
        if self.isEmpty():
            return "Underflow"
        
        else:
            item = self.queue.pop(0)
            
            if (len(self.queue) == 0):
                self.font,self.rear = None
                
            elif (len(self.queue) == 1):
                self.front,self.rear = 0
                
            else:
                self.front = 0
                self.rear = len(self.queue) - 1
                
            return item
        
        
    def Peek(self):
        if self.isEmpty():
            return "Underflow"
        
        else:
            self.front = 0
            return self.queue[self.front]
        

    def Display(self):
        if self.isEmpty():
            return "Queue is Empty"   
        
        else:
            self.front = 0
            self.rear = len(self.queue) - 1
            
            print(self.queue[self.front],"<--- Front")
            
            for i in range(1,self.rear):
                print(self.queue[i])
        
            print(self.queue[self.rear],"<--- Rear")
        
        
q = Queue()

q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)

q.Display()
print('\n')

q.Dequeue()
q.Display()