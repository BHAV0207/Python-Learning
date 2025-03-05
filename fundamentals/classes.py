class Car: 
    def __init__(self , model , year , price):
      self.model = model
      self.year = year
      self.price = price  
    
    def display_info(self):
      print(f"{self.year} {self.model} for {self.price}")
      

car1 = Car("Toyota" , 2019 , 20000)
print(car1.display_info())


# ------------------------------------------- SELF ----------------------------------------------

# Unlike languages like Java or C++, where this is implicit, Python explicitly requires self to refer to instance attributes.python Copy Edit
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Toyota", "Camry")
car1.display_info()  # Output: Car: Toyota Camry
# 🔹 Here, self.brand and self.model refer to the attributes of the specific instance (car1).

# 🔹 How self Works?
# ✅ 1. self Refers to the Current Instance
# Each instance of a class has separate attributes, and self makes sure that we access the correct instance's attributes. python Copy Edit
class Dog:
    def __init__(self, name):
        self.name = name  # Assigning instance variable

    def speak(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

dog1.speak()  # Output: Buddy says Woof!
dog2.speak()  # Output: Charlie says Woof!
# 🔹 self.name ensures that dog1 and dog2 have separate names.



# -------------------------------------------__init__----------------------------------------------

# __init__() Method (Constructor)
# The __init__() method is a constructor.
# It gets called automatically when an object is created.
# It initializes attributes (variables) of an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
print(p1.name)  # Output: Alice
print(p1.age)   # Output: 30
# 🔹 Instance Variables vs Class Variables
# Type	Defined Inside	Scope	Example
# Instance Variable	__init__()	Unique to each object	self.name
# Class Variable	Outside __init__()	Shared across all objects	Car.wheels = 4

class Car:
    wheels = 4  # Class variable (shared by all objects)

    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4 (shared)
print(car2.wheels)  # Output: 4

