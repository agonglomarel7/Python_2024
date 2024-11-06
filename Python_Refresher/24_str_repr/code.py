
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    
    def __str__(self):

        return f"Person '{self.name}' is {self.age} years old"
        
bob = Person("Bob", 14)
print(bob)