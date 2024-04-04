class Person:
    num_of_people = 0       # class attribute / variable

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod    # decorator
    def number_of_people(cls):
        return cls.num_of_people
    
    @classmethod    
    def add_person(cls):
        cls.num_of_people += 1

p1 = Person("Jack")
print(Person.number_of_people())   # Output: 1

p2 = Person("Jill")     
print(Person.number_of_people())   # Output: 2