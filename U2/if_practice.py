# marks = int(input("Enter a Marks : "))
# if marks>= 90:
#     print("You Got A Grade..")
# elif marks>= 75 :
#     print("You Got B Grade..")
# elif marks>= 65 :
#     print("You Got C Grade..")
# else:
#     print("You Got D Grade..")
#
#
#
# ammount = int(input("Enter Ammount : "))
# if ammount > 1000:
#     disc = ammount * 0.10
#     total = ammount - disc
#     print(f"You Got Discount worth {disc} and your total payable ammount is {total}")
#
#
#
# year = int(input("Enter Year : "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")
#
#
#
# age = int(input("Enter Age : "))
# if age < 18:
#     print("You Are Not Eligible")
# elif age >= 18:
#     print("You Are Eligible")
#
#
#
# num = int(input("Enter Number : "))
# if num > 0:
#     print("Positive Number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative Number")
#
#
#
# var = 100
# if var == 200:
#     print("1 - Got a true Expression Value")
#     print(var)
# elif var == 150:
#     print("2 - Got a true Expression Value")
#     print(var)
# elif var == 100:
#     print("3 - Got a true Expression Value")
#     print(var)
# else:
#     print("4 - Got a false Expression Value")
#     print(var)
# print("Good Bye")
#
#
#
# num1 = int(input("Enter Number 1 : "))
# num2 = int(input("Enter Number 2 : "))
# num3 = int(input("Enter Number 3 : "))
# if num1 > num2 and num1 > num3:
#     print(f"Number 1 is Max")
# elif num2 > num1 and num2 > num3:
#     print(f"Number 2 is Max")
# else:
#     print(f"Number 3 is Max")
#
#
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# print("Good Bye")
#
#
#
# count = 0
# while(count < 3):
#     count += 1
#     print("Hello Greek")
# else:
#     print("In Else Block")


# for letter in 'python':
#     print('Current Letter:',letter)
#
#     fruits = ('apple','banana','cherry')
#     for fruit in fruits:
#         print('Current Fruit:',fruit)
#     print("Good Bye")
#
#
#
# for x in range(2,10,2):
#     print(x)



# print("List iteration")
# l = ["geeks","for","geeks"]
# for i in l:
#     print(i)
# 
# print("Tuple iteration")
# t = ("geeks","for","geeks")
# for i in t:
#     print(i)


# for j in [1, 2, 3, 4, 5]:
#     if j == 4:
#         print("Element Found!")
#         break
# print(j)



#a = 0
#while a <= 5:
#    a=a+1
#    if a % 2 == 0 :
#        continue
#    print(a)
#print("End of loop")



# 
# for i in range(5):
#     if i == 3:
#         pass
#     else:
#         print(i)

# str_input = input("Enter a string: ")
# if len(str_input) > 0:
#     print(f"First character: {str_input[0]}")
#     print(f"Last character: {str_input[-1]}")
# else:
#     print("Empty string entered")
#
#
# age = int(input("Enter Your Age: "))
# result = "Age is : " + str(age)
# print(result)
#
# a = input("Enter first string: ")
# b = input("Enter second string: ")
#
# if len(a) > len(b):
#     print("First is longer")
# elif len(b) > len(a):
#     print("Second is longer")
# else:
#     print("Both are equal")

# str1 = input("Enter first string: ")
#
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# if str1[0] in vowels:
#     print("First string starts with a vowel")
# else:
#     print("First string doesn't start with a vowel")

input_string = input("Enter a string to reverse: ")
reversed_string = input_string[::-1]
print(f"Reversed string: {reversed_string}")
