# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
        
#     def add(self,number):
#         real = self.real + number.real
#         imag = self.imag + number.imag
#         result = Complex(real,imag)
#         return result
    
# c1 = Complex(5,2)
# c2 = Complex(4,9)

# result = c1.add(c2)
# print(f"Real = {result.real} and Imaginary = {result.imag}")



# There are two types of variables in Classes:-
# 1. Class/Static variable
# 2.Instance variables

# class Car:
#     wheels = 4  #Class/Static variable
    
#     def __init__(self):
#         self.mil = 10               #Instance variables
#         self.company = "Porsche"    #Instance variables
        
# c1 = Car()
# c2 = Car()

# Car.wheels = 10

# print(c1.company, c1.mil, c1.wheels)
# print(c2.company, c2.mil, c2.wheels)



# There are two types of methods in Classes:-
# 1.Instance methods
# 2. Class methods
# 3.Static methods

class Student:
    school = "KVS"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def average(self):      # Instance method
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod            # Class method
    def getSchoolName(cls):
        return cls.school
    
    @staticmethod              # Static method
    def info():
        print("This is a Student class")
    
    
s1 = Student(21,79,94)
s2 = Student(56,70,88)

Student.info()
print(Student.getSchoolName())
print(s1.average())