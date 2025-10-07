user_id = input("Enter your User ID: ")
user_name = input("Enter your Name: ")


print(f"Original ID: {user_id}")
print(f"Original Name: {user_name}")

print("\n String Operations on User ID ")

print("strip():", user_id.strip())
print("lstrip(''):", user_id.lstrip())
print("rstrip(''):", user_id.rstrip())
print("capitalize():", user_id.capitalize())
print("isalpha():", user_id.isalpha())
print("isalnum():", user_id.isalnum())
print("isdigit():", user_id.isdigit())
print("islower():", user_id.islower())
print("isupper():", user_id.isupper())
print("swapcase():", user_id.swapcase())
print("Count of '0':", user_id.count('0'))
print("Position of '123':", user_id.find('123'))


print("\n String Operations on Name ")

print("strip():", user_name.strip())
print("lstrip():", user_name.lstrip())
print("rstrip():", user_name.rstrip())
print("capitalize():", user_name.capitalize())
print("isalpha():", user_name.isalpha())
print("isalnum():", user_name.isalnum())
print("isdigit():", user_name.isdigit())
print("islower():", user_name.islower())
print("isupper():", user_name.isupper())
print("swapcase():", user_name.swapcase())
print("Count of 'o':", user_name.count('o'))
print("Position of '123':", user_name.find('123'))
