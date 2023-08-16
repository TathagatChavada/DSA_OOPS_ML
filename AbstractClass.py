# from abc import ABC, abstractmethod

# class Computer(ABC):
    
#     @abstractmethod
#     def process(self):
#         print("Processing Data")
    
    
# class Laptop(Computer):
#     def process(self):
#         print("Processing")
        
        
# c1 = Laptop()
# c1.process()

x = [2,4]
y = [0,0]

for i in range(len(x)):
    y[i] = 2 * (x[i])
    
print(y)
