class Student:
    name = "tirth"
    age = 19

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object
student1 = Student()

# Accessing class attributes
print("Name:", student1.name)
print("Age:", student1.age)

# Accessing class method
student1.display()