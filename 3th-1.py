class Dog:
    quantity = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.quantity += 1



bulldog = Dog("sam", 3)
hosky = Dog("Alex", 5)


print(Dog.quantity)
print(hosky.quantity)

