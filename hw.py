# 1. Car Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand, car1.model)

# 2. Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "George Orwell")
print(book1.title, book1.author)

# 3. Laptop Class
class Laptop:
    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

laptop1 = Laptop("Dell", "16GB", "Intel i7")
print(laptop1.brand, laptop1.ram, laptop1.processor)

# 4. Student Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rohit", 20)
student1.age = 21
print(student1.name, student1.age)

# 5. Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("Amit", 50000)
emp1.display_details()

# 6. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rect1 = Rectangle(5, 10)
print("Area:", rect1.area())

# 7. BankAccount Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance}")

account1 = BankAccount("Rahul", 1000)
account1.deposit(500)

# 8. Movie Class
class Movie:
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

movie1 = Movie("Inception", 2010)
movie2 = Movie("Interstellar", 2014)
print(movie1.title, movie1.release_year)
print(movie2.title, movie2.release_year)

# 9. Dog Class
class Dog:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def update_age(self, new_age):
        self.age = new_age

dog1 = Dog("Labrador", 3)
dog1.update_age(4)
print(dog1.breed, dog1.age)

# 10. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(7)
print("Circumference:", circle1.circumference())
