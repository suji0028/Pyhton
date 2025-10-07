cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore", "Hyderabad", "Ahmedabad"]

print(cities[:3])
print(cities[2:6])

cities.insert(3, "Surat")
print(cities)

cities.append("Pune")
print(cities)

cities.remove("Kolkata")
print(cities)

print(cities[::-1])

cities.clear()
print(cities)
