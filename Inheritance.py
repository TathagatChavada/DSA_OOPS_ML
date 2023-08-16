class A:
    def __init__(self):
        print("Init of A")
        
    def feature1(self):
        print("Feature 1 is working")
        
        
    def feature2(self):
        print("Feature 2 is working")
        
        
class B(A):
    
    def __init__(self):
        super().__init__()
        print("Init of B")
        
    def feature3(self):
        print("Feature 3 is working")
        
        
    def feature4(self):
        print("Feature 4 is working")
        

a1 = B()


# Calculates the perimeter of a Polygon
# class Polygon:
#     def __init__(self,*sides):
#         self.lst = [*sides]
        
#     def display_info(self):
#         print("A polygon is a 2-D shape with straight lines")
    
#     def get_preimeter(self):
#         return sum(self.lst)
        
        
# class Triangle(Polygon):
#     def display_info(self):
#         print("A Triangle is a polygon with 3 sides")
        
#         super().display_info()


# class Quadrilateral(Polygon):
#     def display_info(self):
#         print("A Quadrilateral is a polygon with 4 sides")


# t1 = Triangle(3,4,5)
# perimeter = t1.get_preimeter()
# t1.display_info()
# print(f"Perimeter of a triangle is {perimeter}")
