# fun1 = lambda a,b: a+b
# fun = lambda a: a*a
#
# res1 = fun1(10,20)
# res2 = fun(10)
#
# print("Square is: ",res2)
# print("Sum is: ",res1)


check_odd_even = lambda x: "Even" if x % 2 == 0 else "Odd"

number = 8
result = check_odd_even(number)
print(f"{number} is {result}")
