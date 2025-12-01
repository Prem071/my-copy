

user_loc = (17.4941466,78.3918427) #JNTU
d1_loc = (17.4440231,78.5061319) #Kukatpally
d2_loc = (17.4964542,78.370361) #JNTU

def dist(point_1, point_2):

    total_dist = ((point_2[0] - point_1[0])**2) + ((point_2[1] - point_1[1])**2)**0.5

    return total_dist


def driverAssign(user, d1, d2):
    if dist(user, d1) < dist(user, d2):
        print("Driver - 1 Assigned")
    else:
        print("Driver - 2 Assigned")

driverAssign(user_loc, d1_loc, d2_loc)

import math

print(math.dist(user_loc, d1_loc))
print("----------------------------")
print(dist(user_loc, d1_loc))



