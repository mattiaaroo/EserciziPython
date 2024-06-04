#Pizzas
pizzasList: list = ["margherita", "diavola", "quattro formaggi"]
phrasesList: list = [" is the simplest pizza", " is the american ppperoni", " has four different chees types"]
pizzasDict : dict = dict(zip(pizzasList, phrasesList))
for k, v in pizzasDict.items():
    print(f"{k}{v}")
print("I love to have a dinner with my friends just to try new pizza' spots")
print("I really love pizza")


print("\n")
#Animals
animals: list = ["lion", "tiger", "leopard"]
phrasesList: list = [" is a very dominant animal", " is a solitary hunter", " is a very agile climber"]
animalsDict : dict = dict(zip(animals, phrasesList))
for k, v in animalsDict.items():
    print(f"{k}{v}")
print("all this animals carnivores")

print("\n")
#Counting to twenty 
for num in range(1,21):
    print(num)

print("\n")
#One Million
oneMillion: list = []
for num in range(1, 1000001):
    oneMillion.append(num)
print(oneMillion)

print("\n")
#Summing a Million
oneMillion: list = []
for num in range(1, 1000001):
    oneMillion.append(num)
print("\n")
print(min(oneMillion), max(oneMillion))
print("\n")
print(sum(oneMillion))

print("\n")
#Odd Number
lista20dispari: list = []
for num in range(1, 21, 2):
    lista20dispari.append(num)
print(lista20dispari)

print("\n")
#Threes
threes: list = []
for num in range(3, 31, 3):
    threes.append(num)
print(threes)

print("\n")
#Cubes
cubes: list = []
for num in range (1, 11):
    num = num**3
    cubes.append(num)
print(cubes)

print("\n")
#Cube Comprhension
cubes: list = [num**3 for num in range(1, 11)]
print(cubes)

print("\n")
#Slices
cubes: list = [num**3 for num in range(1, 11)]
print(cubes)
print(cubes[:3])
print(cubes[3:7])
print(cubes[-3:])

print("\n")
#My Pizzas, Your Pizza
'''
pizzasList: list = ["margherita", "diavola", "quattro formaggi"]
phrasesList: list = [" is the simplest pizza", " is the american ppperoni", " has four different chees types"]
pizzasDict : dict = dict(zip(pizzasList, phrasesList))
for k, v in pizzasDict.items():
    print(f"{k}{v}")
print("I love to have a dinner with my friends just to try new pizza' spots")
print("I really love pizza")'''
pizzasList: list = ["margherita", "diavola", "quattro formaggi"]
friend_pizzas: list = ["margherita", "diavola", "quattro formaggi"]
pizzasList.append("bianca")
friend_pizzas.append("rustica")
print("My favourite pizzas are: ")
for pizza in pizzasList:
    print(pizza)
print("My friend favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)

print("\n")
#More Loops
for pizza in pizzasList:
    print(pizza)
for pizza in friend_pizzas:
    print(pizza)

print("\n")
#Conditional Tests
car = 'evo 3'
print("\n")
print("Is car == 'impreza'? I predict True.")
print(car == 'impreza')
print("\n")
print("\nIs car == 'mini'? I predict False.")
print(car == 'mini')
print("\n")
print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')
print("\n")
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')
print("\n")
print("\nIs lenght of word 'car' more than 4? I predict False.")
print(len(car) > 4)
print("\n")
print("\nIs car in ['gallardo', 'camaro', 'supra']? I predict True.")
print(car in ['gallardo', 'camaro', 'supra'])
print("\n")
print("\nIs car not in ['fiat', 'mercedes', 'toyota']? I predict True.")
print(car not in ['fiat', 'mercedes', 'toyota'])
print("\n")
print("\nIs car == 'SUBARU'? I predict False.")
print(car == 'SUBARU') 
print("\n")
print("\nIs 7 + 5 == 12? I predict True.")
print(7 + 5 == 12)
print("\n")
print("\nIs 21 < 40? I predict True.")
print(21 < 40)


print("\n")