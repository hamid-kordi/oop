class Employee:
    slary = 2000

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    @property
    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    @fullname.setter
    def fullname(self, name):
        self.firstname, self.lastname = name.split(" ")

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None


emp = Employee("ahmad", "majaid")

print(emp.fullname)
emp.fullname = "salam ohmi"
print(emp.fullname)
del emp.fullname
print(emp.fullname)
