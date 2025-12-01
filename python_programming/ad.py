# cities = ["Venice", "Tokyo", "Delhi", "Dubai", 
#           "Chennai", "Benguluru", 
#           "Sao Paulo", "Munich"]


numbers_ = [12,23,80,65,3]

class Rectangle:

    shape = "2D Rectangle"

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getLenght(self):
        return self.length
    
    def getBreadth(self):
        return self.breadth
    
    def areaRect(self):
        return self.length * self.breadth
    
my_rectangle = Rectangle(10,10) 
oth_rectangle = Rectangle(5,5)

print(my_rectangle.length)


# a_ = oth_rectangle.areaRect()
# print(a_)