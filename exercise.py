# Gaetano so già che è sbagliato ma mi confondo troppo

class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs}")

    def return_legs(self):
        return self._number_of_legs
        
animal= Animal()
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs)

class Dog (Animal):
    def __init__(self, name, legs_count):
        Animal.__init__(self, name, legs_count)
        
    def bark(self):
        print("woof woof")

dog = Dog = ("Bob", 4)

dog.bark()
print(dog.legs_count)