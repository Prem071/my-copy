

# cities = ["Venice", "Tokyo", "Delhi", "Dubai", 
#           "Chennai", "Benguluru", "Sao Paulo", "Munich"]


# print(cities[9])

#1. Index Error
#2. Division Error
#


# mobile_sales = 10000
# total_sales = 0

# print(mobile_sales/total_sales)


# lst = [x for x in range(5)]

# lst.append(100)

# print(lst)


# mobile_sales = 10000
# total_sales = 0

# try: 
#     team_percent = mobile_sales/total_sales
# except:
#     print("Invalid Total Sales Value")


# cities = ["Venice", "Tokyo", "Delhi", "Dubai", 
#           "Chennai", "Benguluru", "Sao Paulo", "Munich"]

# try: 
#     print(cities[2])

# except:
#     print("Range out of list!")



# print(10+"Tokyo")


# cv_ = int("Five")
# print(cv_)





# def cube(x) -> int:

#     return x **3 


# print(cube("F"))



def cube(x):
    if x < 0:
        raise ValueError("Input cannot be negative!")
    else:
        return x**3

print(cube(-2))