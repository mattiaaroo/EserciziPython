'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(alice.age)

persone = [alice, bob, Person("Bardh", 28), Person("Walter", 32), Person("Francesca", 25)]
print(persone)
min_age: int = float('inf')
index_min_age: int = 0
for i in range(len(persone)):
    if persone[i].age < min_age:
        min_age = persone[i].age
        index_min_age = i
persona = persone[index_min_age]
print(f'Nome persona più giovane: {persona.name}', f'Età: {min_age}')


class Student:
    def __init__(self, name, studyProgram):
        self.name = name
        self.studyProgram = studyProgram

    def classe(self):
        return (f"Nome: {self.name} Programma: {self.studyProgram}")

    def printInfo(self):
        return self.classe()

    def set_age(self, newAge):
        self.age: int = newAge
    
    def set_gender(self, newGender):
        self.gender: str = newGender

mattia = Student("mattia", "python")
angelo = Student("angelo", "cpp")
marco = Student("marco", "java")

print(mattia.printInfo())
print(angelo.printInfo())
print(marco.printInfo())


class Animal:
    def __init__(self, animal):
        self.animal: str = animal

    def set_legs(self, legs):
        self.legs: int = legs

    def get_legs(self):
        return f"n Legs: {self.legs}"

    def printInfo(self):
        return f"Animal: {self.animal},"
    
cat = Animal("cat")
stambecco = Animal("stambecco")
    
cat.legs = 4
stambecco.legs = 2

print(cat.printInfo(), cat.get_legs())
print(stambecco.printInfo(), stambecco.get_legs())
'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print (f'restaurant name: {self.restaurant_name}, cuisine type: {self.cuisine_type}')
    
    def open_restaurant(self):
        print (f'{self.restaurant_name} is open')
    
Restaurant1 = Restaurant('mamma mia', 'cucina italiana')
Restaurant1.describe_restaurant()
Restaurant1.open_restaurant()

Restaurant2 = Restaurant('tonys pizza', 'exclusively pizza')
Restaurant2.describe_restaurant()
Restaurant3 = Restaurant('taihstant', 'taihlandees')
Restaurant3.describe_restaurant()