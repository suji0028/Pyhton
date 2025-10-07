"""
class bike:
    name = ""
    gear = 0

b1 = bike()

b1.name = "z900"
b1.gear = 6

print(f"Name:{b1.name} Gears:{b1.gear}")

print(b1.name)
print(b1.gear)
"""


"""
class Employee:
    employee_id = 0

employee1 = Employee()
employee2 = Employee()

employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")
"""


"""
class student:
    name = ""
    id = 0
    marks = 0

s1 = student()
s2 = student()
s3 = student()

s1.id = 101
s1.name = "sujal"
s1.marks = 90

s2.id = 102
s2.name = "jal"
s2.marks = 80

s3.id = 101
s3.name = "sachin"
s3.marks = 70

print(f"Student_Name: {s1.name} \nStudent_ID: {s1.id} \nStudent_Marks: {s1.marks}")
print(f"\nStudent_Name: {s2.name} \nStudent_ID: {s2.id} \nStudent_Marks: {s2.marks}")
print(f"\nStudent_Name: {s3.name} \nStudent_ID: {s3.id} \nStudent_Marks: {s3.marks}")
"""


"""
class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        print("Area of room = ",self.length*self.breadth)

study_room = Room()
living_room = Room()
study_room.length = 42.5
study_room.breadth = 30.8
living_room.length = 40.5
living_room.breadth = 30.5

study_room.calculate_area()
living_room.calculate_area()
"""

'''
#with constructor
class bike:
    def __init__(self, name="fz", gear=10):
        self.name = name
        self.gear = gear
        
b1 = bike("M1000", 6)
b2 = bike("S1000", 5)


b3 = bike()

print(f"Name: {b1.name}, Gear: {b1.gear}")
print(f"Name: {b2.name}, Gear: {b2.gear}")
print(f"Name: {b3.name}, Gear: {b3.gear}")
'''


'''
#parent class
class Animal:
    def speak(self):
        print("Animal Makes Sound")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog Barks")

#creating object of child class
dog = Dog()
dog.speak()     #inherited method from Animal
dog.bark()      #Dog's own method
'''


'''
class Animal:
    def eat(self):
        print("Animal Eats")

class Mammel(Animal):
    def walk(self):
        print("Mammal Walks")

class Dog(Mammel):
    def bark(self):
        print("Dog Barks")

#object of Dog class
dog = Dog()
dog.eat()       # From Animal
dog.walk()      # From Mammel
dog.bark()      # From Dog
'''

'''
#Base Class Person
class Person:
    def __init__(self, name):
        self.name=name
#Derived class: Employee -> inherits Person
class Employee(Person):
    def show_role(self):
        print(self.name, "is an employee")
# Derived class: Manager -> inherits Employee
class manager(Employee):
    def department(self,dept):
        print(self.name,"manages",dept,"department")

man = manager("joy")
man.show_role()
man.department("IT")
'''


'''
class Father:
    def skill(self):
        print("Father's Skill: Driving")

class Mother:
    def skill(self):
        print("Mother's Skill: Cooking")

class Child(Father,Mother):
    def own_skill(self):
        print("Child's Skill: Playing")

    def skills(self):
        super().skill()
        Mother.skill(self)
        self.own_skill()

#Object of Child
c = Child()
c.skills()
'''


'''
#Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Animal Eats")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

class Cat(Animal):
    def meow(self):
        print("Cat Meows")

#objects of child classes

dog = Dog()
cat = Cat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()
'''


'''
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is An animal")

class Dog(Animal):
    def __init__(self, name, breed):
        #Call Parent class constructor
        super().__init__(name)
        self.breed = breed
        print(f"{self.name} is a {self.breed} ")

#creating object
dog = Dog("Fido", "Labrador")
'''

'''
#compile time polymorphism
class Calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c

calc = Calculator()

print(calc.add(10,20,30))
print(calc.add(10,20))
print(calc.add(10))
'''


'''
#runtime polymorphism
class Animal:
    def sound(self):
        print("Animal makes different sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

#creating objects
animal = Animal()
dog = Dog()
cat = Cat()

#runtime poly
for obj in (animal,dog,cat):
    obj.sound()  #method call resolved at runtime
'''


class Student:
    def __init__(self, rollno=0, name="", mark1=0, mark2=0, mark3=0):        
        self.rollno = rollno
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total = self.mark1 + self.mark2 + self.mark3
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        per = (self.total / 300) * 100  
        
        if per >= 90:
            return 'A+'
        elif per >= 80:
            return 'A'
        elif per >= 70:
            return 'B+'
        elif per >= 60:
            return 'B'
        elif per >= 50:
            return 'C'
        elif per >= 40:
            return 'D'
        else:
            return 'F'

    def getdata(self):
        print("STUDENT INFORMATION")
        print(f"Roll Number    : {self.rollno}")
        print(f"Name           : {self.name}")
        print(f"Subject 1 Marks: {self.mark1}")
        print(f"Subject 2 Marks: {self.mark2}")
        print(f"Subject 3 Marks: {self.mark3}")
        print(f"Total Marks    : {self.total}/300")
        print(f"Percentage     : {(self.total/300)*100:.2f}%")
        print(f"Grade          : {self.grade}")


student1 = Student(101, "Pal", 85, 92, 78)

print("STUDENT RECORDS:")
print()

student1.getdata()
print()
