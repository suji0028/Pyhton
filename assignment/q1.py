fruits = ["apple", "banana", "cherry", "date", "kiwi", "orange", "mango"]

print(fruits[0:1])
print(fruits[-1:])
print(fruits[1:-1])

fruits.append("grapes")
print(fruits)

fruits.insert(2, "lemon")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.clear()
print(fruits)
