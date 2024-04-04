class Pet:      # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        
    def speak(self):
        print("speak() called from parent class.")

class Cat(Pet):     # Child class      
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.  My fur is {self.color}.")

    def speak(self):
        print("Meow")

class Dog(Pet):     # Child class
    def speak(self):
        print("Woof! Woof!")


p = Pet("Jill", 3)
p.show()
p.speak()

c = Cat("Tom", 5, "White")
c.show()
c.speak()

d = Dog("Buck", 7)
d.show()
d.speak() 