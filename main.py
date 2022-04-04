#Exercise 1
def count_vowels(text):
    vowels = "aeiou"
    text = text.casefold()
    count = {}.fromkeys(vowels, 0)
    for i in text:
        if i in count:
            count[i] += 1
            return count
    else:
        return 42

#Exercise 3
class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type
        __call__ = self


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors
    def __str__(self):
        return print("Color:", self.color, "Fuel Type:", self.fuel_type, "Doors:", self.doors)


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super(). __init__ (color, fuel_type)
        self.passengers = passengers
    def __str__(self):
        return print("Color:", self.color, "Fuel Type:", self.fuel_type, "Passengers", self.passengers)

#car1 = Car("red", "gas", "four") - practise

#Exercise 4
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __str__(self):
            return print(self.name, ",", self.author)


#book1 = Book("Dune", "Franke Herbert") - more practise


