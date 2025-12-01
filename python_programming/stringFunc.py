
first_name = 'Phones are getting expensive'

# print(first_name)
# print(first_name.strip())
# print(first_name.replace(" ", ""))

# name_ = input("Enter the Name: ")
# city = input("Enter the City: ")


cust_name = "Kenney"
merchant_ = "Bharat Petrol"
trans_amt = 550
acc_bal = 50000


# greeting_ = f'''Dear {cust_name}, a transaction of {trans_amt} 
#             has been done to {merchant_}. 
#             Current Balance: {acc_bal}'''


greeting_ = '''Dear {0}, a transaction of {1} 
            has been done to {2}. 
            Current Balance: {3}. 
            Hope you have a good day {0}'''.format(cust_name, trans_amt, merchant_, acc_bal)


print(greeting_)

# greeting = "Hello"

print("123".isnumeric())