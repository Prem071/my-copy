




#isalpa() -- True ONLY when all the characters are Alphapets, else False

#isdigit() -- True when all the characters are NUMBERS, else False

#isalnum() -- True when we have atleast ONE number in the string

# print("A".isalnum())

#1. Characters
#2. Mix of Alphabets & Number
#3. Atleast one Special Character
#4. Should not contain Spaces
#5. Mix of Both Upper and Lower. (Ops)


password_ = "John"
if len(password_) < 8:
    print("Password Must Contain min 8 Characters")
elif password_.isdigit():
    print("Password Must Contain Alphabets")
elif password_.isalpha():
    print("Password Must Contain Numbers")
elif password_.count("@") == 0 and password_.count("#") == 0 and password_.count("$") == 0 and password_.count("_") == 0:
    print("Pasword must contain special Characters (@#$_)")
elif password_.count(" ") > 0:
    print("Password Cannot have spaces")
else:
    print("Password is Valid!")





isNum = 
isAlpha = 
isLong = 
isSpaceFree = 
isSpecial = 


if True:

    print("Valid Password")

else:

    print






