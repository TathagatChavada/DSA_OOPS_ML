class Deque:
    
    def __init__(self):
        self.deque = []
        
        
    def isEmpty(self):
        return len(self.deque) == []
    
    
    def addFront(self,item):
        self.deque.insert(0, item)
        
        
    def addRear(self, item):
        self.deque.append(item)
        
        
    def removeFront(self):
        if self.isEmpty():
            return "Deque is Empty"
            
        return self.deque.pop(0)
     
     
    def removeRear(self):
        if self.isEmpty():
            return "Deque is Empty"
        
        return self.deque.pop()
        
        
        
d = Deque()
print(d.isEmpty())

d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
d.addRear(11)

print(d.removeRear())
print(d.removeFront())

d.addFront(55)
d.addRear(45)

print(d.deque)