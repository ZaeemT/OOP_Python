class Person:
    num_of_people = 0       # class attribute / variable

    def __init__(self, name):
        self.name = name
        Person.num_of_people += 1

p1 = Person("Jack")
print(Person.num_of_people)   # Output: 1

p2 = Person("Jill")     
print(Person.num_of_people)   # Output: 2