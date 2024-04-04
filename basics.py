class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
        #print(self.name)

    def get_age(self):
        print(self.age)

    def set_age(self, x):
        self.age = x

d = Dog("Bob", 12)

print(d.get_name())
d.get_age()

d.set_age(5)
d.get_age()
