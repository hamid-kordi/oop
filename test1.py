class Student:
    school_name = "ABC IRAN"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ful():
        return "hello"
    def fullf(self):
        return "hi"
    

    def show(self):
        print("Student:", self.name, self.age, Student.school_name)

    def __str__(self):
        return f"self.name -->  self.age"

    def change_age(self, new_age):

        self.age = new_age

    @classmethod
    def modify_school_name(cls, new_name):

        cls.school_name = new_name

gh = Student("name",34)

print(Student.ful())
print(gh.fullf())
# s1 = Student("Harry", 12)
# s2 = Student("ahmad", 15)

# s2.__str__()
# s1.show()
# s1.change_age(14)

# Student.modify_school_name("XYZ School")
# s1.show()
