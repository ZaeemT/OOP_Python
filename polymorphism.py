class Language: # Abstract class
    def greet(self):
        raise NotImplementedError("Use greet() in child class")
    
class French(Language):
    def greet(self):
        print("Greeting in French")

class Chinese(Language):
    def greet(self):
        print("Greeting in Chinese")

def intro(lang):
    lang.greet()

a = French()
b = Chinese()

intro(a)
intro(b)
