from abc import ABC, abstractmethod

# ============================================
# OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
# ============================================

# 1. CLASS
# Definition: A blueprint for creating objects. It defines attributes and methods.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  def display_info(self):
    return f"{self.brand} {self.model}"

car1 = Car("Toyota", "Camry")
print(car1.display_info())  # Output: Toyota Camry


# 2. OBJECT/INSTANCE
# Definition: An instance of a class. A concrete realization of the blueprint.
car2 = Car("Honda", "Civic")


# 3. ENCAPSULATION
# Definition: Bundling data (attributes) and methods together, hiding internal details.
class BankAccount:
  def __init__(self, balance):
    self.__balance = balance  # Private attribute (__)
  
  def deposit(self, amount):
    self.__balance += amount
  
  def get_balance(self):
    return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500


# 4. INHERITANCE
# Definition: A class can inherit attributes and methods from another class.
class Animal:
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    return "Some sound"

class Dog(Animal):
  def speak(self):
    return f"{self.name} barks: Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks: Woof!


# 5. POLYMORPHISM
# Definition: Objects can take multiple forms. Same method name, different behavior.
class Cat(Animal):
  def speak(self):
    return f"{self.name} meows: Meow!"

animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
  print(animal.speak())  # Different output for each type


# 6. ABSTRACTION
# Definition: Hiding complex implementation details and showing only essential features.

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5