# student_id = {112,114,116,118,115}
# print("Student Id: ",student_id)
#
# vowel_letters = {'a','e','i','o','u'}
# print("Vowel Letters: ",vowel_letters)
#
# mixed_set = {112,'a',114,116,'e'}
# print("Mixed Set: ",mixed_set)
#
# duplicate_set = {112,112,114,116,118,115}
# print("Duplicate Set: ",duplicate_set)
#
# student_id.add(119)
# student_id.remove(115)
# student_id.discard(118)
# vowel_letters.update(['A','E','I','O','U'])
# popped_value = student_id.pop()
# print("Popped Value: ",popped_value)
# print("Student Id: ",student_id)
# print("After Changing Values:",student_id, vowel_letters, mixed_set)
# print(len(student_id))
# student_id.clear()

A = {1,2,3,4,5}
B = {4,5,6,7,8}

union_set = A.union(B)
print("Union Set: ",union_set)
intersection_set = A.intersection(B)
print("Intersection Set: ",intersection_set)
difference_set = A.difference(B)
print("Difference Set: ",difference_set)
symmetric_difference_set = A.symmetric_difference(B)
print("Symmetric Difference Set: ",symmetric_difference_set)

# empty_set = set()
# empty_dict = { }
# print(type(empty_set))
# print(type(empty_dict))

set1 = {10, 3, 1, "Abhi", True, 2.5}
print(set1)

set11 = set({12, 3, 6})
print(set11)

set2 = {10, 3, 1, "Abhi", True, 2.5, 1}
print(set2)

set3 = {}
print(set3)

print(type(set3))
print(type(set2))

set4 = set()
print(type(set4))

# Can't modify a set by indexing or item assignment (sets are unordered)
# The following would raise an error, so it is intentionally commented out:
# set1[2] = 99

print(set1)

# length of set
print(len(set1))

# Tuple can be added (immutable)
set1.add((2, 7, 50))
print(set1)

# Lists are unhashable (mutable), so convert to a tuple before adding
set1.add((2, 7, 22))
print(set1)


