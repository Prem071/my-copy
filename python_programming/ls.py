
# squres = []
# for num in range(1, 51):
#     squres.append(num**2)

# print(squres)

squares = [ num**2  for num in range(1,51)]
print(squares)


# square = {}
# for i in range(10):
#     square[i] = i**2

# sq_dict = {num : num**2 for num in range(10)}
# print(sq_dict)

cities = ["Venice", "Tokyo", "Delhi", "Dubai", 
          "Chennai", "Benguluru", "Sao Paulo", "Munich"]


# upper = []
# for i in cities:
#     upper.append(i.upper())

# print(upper)



# upper_1 = [i.upper()  for i in cities]
# print(upper_1)


# ones_1 = [100 for i in range(20)]
# print(ones_1)


# ones_1 = {i:0 for i in range(20)}
# print(ones_1)

# even_squares = []
# for i in range(20):
#     if i%2 == 0:

#         even_squares.append(i**2)

# print(even_squares)



print([x**2 for x in range(20) if x%2 == 0])