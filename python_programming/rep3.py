

# a = 0
# odd_numbers = []
# while a < 100:
#     if a%2 != 0:
#         odd_numbers.append(a)
#     else:
#         continue

#     a = a + 1
    
# print(odd_numbers)

letter_ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
even_index = []
odd_index = []
a = 0
while a < 8:
    if a%2 == 0:
        even_index.append(letter_[a])
    else:
        odd_index.append(letter_[a])
    a = a + 1

print(even_index, odd_index)

