
#Q1: Store odd numbers from 0-100 in a list




a = 0
odd_numbers = []
while a < 100:
    if a%2 != 0:
        odd_numbers.append(a)
    else:
        continue

    a = a + 1
    
print(odd_numbers)