# Types of Polymorphism are:-
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading:Two different methods with same name but different argument types.
# 4. Method Overriding

# 1. Duck Typing
# If there is a bird that beahaves like a duck,
# quacks like a duck, walks like a duck, it swims like a duck it will be a duck
class VsCode:
    def execute(self):
        print("Executing")
        print("Running")
        
        
class MyEditor:
    def execute(self):
        print("AutoCompleting")
        print("Executing")
        print("Running")
        
class Laptop:
    def code(self,ide):
        ide.execute()
        
ide = VsCode()

lap1 = Laptop()
lap1.code(ide)
print()

# Operator Overloading
#  The same operator to have different meaning 
#  according to the context is called operator overloading.
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        
        return s3
    
    def __str__(self) -> str:
        return f"{self.m1}, {self.m2}"
        
        

s1 = Student(68,97)
s2 = Student(78,88)

s3 = s1 + s2        # s1.__add__(s2)  --> Student.__add__(s1,s2)
print(s3.m1)

print(s1.__str__())