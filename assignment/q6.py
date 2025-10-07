# 1. Create a list of 5 numbers and print each element using a loop
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)

# 2. Add 60 to the end using append()
numbers.append(60)
print(numbers)

# 3. Insert 15 at index 1
numbers.insert(1, 15)
print(numbers)

# 4. Remove 30 from the list
numbers.remove(30)
print(numbers)

# 5. Sort in ascending order
numbers.sort()
print(numbers)

# 6. Reverse the list
numbers.reverse()
print(numbers)

# 7. Create a fruits list and print first three using slicing
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print(fruits[:3])

# 8. Copy a list using slicing
copy_fruits = fruits[:]
copy_fruits.append("grapes")
print("Original:", fruits)
print("Copied:", copy_fruits)

# 9. Create student list and print names from index 1 to 4
students = ["Amit", "Beena", "Chirag", "Divya", "Esha", "Farhan"]
print(students[1:5])

# 10. Clear all elements from a list
students.clear()
print(students)
