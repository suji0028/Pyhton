"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = a/b
print("a/b = %d" %c)
print("Hi i am other part of the program")
"""

"""
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)
except :
    print("Can't divide by zero")
"""

"""
try:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    c = a/b
    print("a/b = %d"%c)

except Exception:
    print("cant divide by 0")
    print(Exception)
else:
    print("Hi i am else block")
"""

"""
try:
    fileptr  = open("hello.txt","r")
    print(fileptr.read())

except IOError:
    print("File not found")
else:
    print("File open successfully")
    fileptr.close()
"""

# try:
#     a = 10/0
# except(ArithmeticError, IOError):
#     print("Arithmetic Exception ")
# else:
#     print("Successfully Done")


# try:
#     fh = open("testfile","w")
#     try:
#         fh.write("This is my test file for except")
#     finally:
#         print("Going to close the file.")
#         fh.close()
# except IOError:
#     print("Error: can't find file or read data")


# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError as ve:
#         print("the argument does not contain numbers\n ",ve.args)
#
# temp_convert("xyz")

"""
try:
    age = int(input("Enter the age:"))
    if(age<18):
        raise ValueError
    else:
        print("Age is valid")
except ValueError:
"""



# try:
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     if b is 0:
#         raise ArithmeticError
#     else:
#         print("a/b = %d"%(a/b))
# except ArithmeticError:
#     print("Can't divide by zero")
#     print("The age is not valid")


# try:
#     a = int(input("Enter a: "))
#     if a <= 0 :
#         raise ValueError("Negative number or zero not allowed")
#     else:
#         print("You entered a positive number")
# except ValueError as ve:
#     print("Number Must Be Positive",ve)

# import re
# pattern = r"world"
# text = "Hello,World!"
#
# match = re.search(pattern,text)
# if match:
#     print("Found a match!")
#
# else:
#     print("Not matched")

import re
pattern = r"R"
text = "hello,world!"

if re.match(pattern,text):
    print("Found a match!")
else:
    print("Not matched")
