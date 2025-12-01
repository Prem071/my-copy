class Point:


    def __init__(self, x, y):
        self.x = x
        self.y = y



    def distance(self, oth_point):

        return ((oth_point.x - self.x)**2 + (oth_point.y-self.y)**2)**0.5





    



p1 = Point(1,2)
p2 = Point(3,5)

print(p1.distance(p2))



import shapely 

V = shapely.Point(1,2)
U = shapely.Point(3,5)

print(V.distance(U))