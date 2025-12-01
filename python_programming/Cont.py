cities = ["Venice", "Tokyo", "Delhi", "Dubai", 
          "Chennai", "Benguluru", "Sao Paulo", "Munich"]

# print(len(cities))

# print(cities[::(len(cities)-2)+1])

print(cities)

# cities.append('Jersey')

# cities_2 = ['Jersey', 'Abu Dabi']

# cities.append(cities_2)

# cities.extend(cities_2)

# cities.insert(0, 'Jersey')

# import time


# cities.pop(0)

# for i in range(10):
#     if len(cities) > 0:
#         cities.pop()
#         print(cities)
#         time.sleep(2)
#     else:

#         print("List is Empty!")
    
#     print("---------------------")

cities = ["Venice", "Tokyo", "Delhi", "Dubai", 
          "Chennai", "Benguluru", "Sao Paulo", "Munich"]


input_user = input("Enter the name of the city: ")
if cities.count(input_user) > 0:
    print("Value Exists!")

else:
    print("Value Does not Exists!")









#Q2: Check if an element exists in the list. 

# cities_3 = cities + cities_2

# print(cities_3[-1][1][0])
# print(cities.count('Venice'))


