

def quadrantTest(x,y):


    if x > 0 and y > 0:

        print("Point Lies in the Q-I")

    elif x < 0 and y > 0:

        print("Point Lies in the Q-II")

    elif x < 0 and y < 0:

        print("Point Lies in the Q-III")

    else: 
        print("Point Lies in the Q-IV")



quadrantTest(-2,3)


def quadrantTest(x,y):


    if x > 0 and y > 0:
        quadrant = 1 

    elif x < 0 and y > 0:
        quadrant = 2 

    elif x < 0 and y < 0:
        quadrant = 3 

    else: 
        quadrant = 4


    return quadrant


quadrantTest(-2,3)


'''

Q1: Function which takes 
any two numbers and
operation as the input  
and return the result
Eg: a, b, subtraction

'''

