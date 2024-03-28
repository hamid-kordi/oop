class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"my name is {self.name},and i am {self.age} years old"


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def displayStudent(self):
        return f"{self.name}<->{self.age}<->{self.major}"



emp1 = Student("salar", 33, "teacher")


print(emp1.display())
print(emp1.displayStudent())
