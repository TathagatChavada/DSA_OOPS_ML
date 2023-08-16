# a = 10

# def add():
#     global a
#     a = a + 10
#     print(a)
    

# print(a)
# add()

def smart_divide(func):
    
    def inner_func(a,b):
        if b == 0:
            print("Cannot divide by 0")
            return
        
        return func(a,b)
    
    return inner_func


@smart_divide
def divide(a,b):
    print(a/b)
    
divide(20,2)
divide(10,0)