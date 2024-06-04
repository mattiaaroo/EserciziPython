# Mattia Ro' 
# 18/04/2024

import random
'''
print("Hello World!")

print("\n")
#Personal Message 1 - 2
name: str = "Eric"
print(f"Hello {name}, how are you?")
print(f"Hello {name}, would you like to learn some Python today")

print("\n")
#Name Cases
upperCases = name.upper()
lowerCases = name.lower()
print(upperCases)
print(lowerCases)

print("\n")
#Famouse Quote 1 - 2
"Martin Luther King once said: I have a dream"
message = "I have a dream"
famousPerson = "Martin Luher King"
print (message + " once said "  + famousPerson)

print("\n")
#File Extension
fileName = "python_notes.txt"
correctFileName = fileName.removesuffix(".txt")
print(correctFileName)

print("\n")
#Names
names = ["Gianni", "Mario", "Flavio", "Andrea", "Matteo"]
friend1 = names[0]
friend2 = names[1]
friend3 = names[2]
friend4 = names[3]
friend5 = names[4]
listaAmici = [friend1, friend2, friend3, friend4, friend5] #questa lista è stata creata solo a scopo per un check
print (listaAmici)

print("\n")
#Greetings
for name in names:
    print ("Grazie mille per aver partecipato all'attività", name )

print("\n")
#Your own list
vehicles = ["an S2000", "an s13", "an honda civic", "a mitsubishi evo", "a mitsubishi lancer", "an harley davinson"]
for vehicle in vehicles:
    print("Surely " + vehicle + " is in my dream garage")

print("\n")
#Guest List
guestList: list = ["Micheal Jackson", "Al Bano", "Ed Sheeran", "Giorgio Caldarelli"]
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)

print("\n")
#Changing Guest List
guestList: list = ["Micheal Jackson", "Al Bano", "Ed Sheeran", "Giorgio Caldarelli"]
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)
NMAguest: str = guestList[0]
print(NMAguest)
guestList.remove(NMAguest)
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)

print("\n")
#More Guest
guestList: list = ["Micheal Jackson", "Al Bano", "Ed Sheeran", "Giorgio Caldarelli"]
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)
NMAguest: str = guestList[0]
print(NMAguest)
guestList.remove(NMAguest)
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)
print("Good news guys: I just found a bigger table")
guestList.insert(0,"Travis Scott")
guestList.insert(2, "Romina Power")
guestList.append("Mario Rossi")
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)


print("\n")
#Shriking Guest List
guestList: list = ["Micheal Jackson", "Al Bano", "Ed Sheeran", "Giorgio Caldarelli"]
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)
NMAguest: str = guestList[0]
print(NMAguest)
guestList.remove(NMAguest)
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)
print("Good news guys: I just found a bigger table")
guestList.insert(0,"Travis Scott")
guestList.insert(2, "Romina Power")
guestList.append("Mario Rossi")
print("\n")
for guest in guestList:
    message: str = "Ciao " + guest + ", sono felice di invitarti questa sera a cena per festeggiare il mio compleanno"
    print(message)
print("I'm sorry guys but I've just found out I have not enough space to host you all, so I can invite only 2 of you")
while len(guestList) > 2:
    guestList.pop(0)
    if len(guestList) == 2:
        print(f"Here's the updated 2 members list: {guestList}")
        for guest in guestList: 
            print(f"Hey {guest} fortunately you're still invited to the dinner see you tonight")

while len(guestList) != 0:
    del guestList[0]
print(guestList)

print("\n")
#Seeing the world
Locations: list = ["New York", "Tokyo", "City of Mexico", "Niagara Falls", "Naples"]
print(Locations)
sortedList: list = []
print("\n")
for location in Locations:
    sortedList.append(location)
sortedList.sort()
print(sortedList)
print(Locations)
RsortedList: list = []
print("\n")
for element in sortedList:
    RsortedList.insert(0,element)
print(RsortedList)
print(Locations)
print("\n")
reversed: list = []
for element in sortedList:
    reversed.insert(0,element)
reversed.reverse()
print(reversed)
print(Locations)
print("\n")
reversed.reverse()
print(reversed)
print(Locations)
print("\n")
Locations.sort()
print(Locations)
print("\n")
Locations.reverse()
print(Locations)

print("\n")
#Dinner Guests
finalGuestNumber: int = len(guestList)
print(f"Il numero finale degli invitati è: {finalGuestNumber}")

print("\n")
#Every Function
listLength: int = input(print("Definisci la lunghezza della tua lista: "))
print("\n")
posizione: int = 0
while posizione <= listLength:
    elem: str = (input(print("Inserisci l'elemento in posizione: {posizione} ")))
print("\n")
#Person
persona: dict = {"first_name": "Mattia", "last_name": "Ro'", "age": 19, "city": "Roma"}
print(persona)
for k in persona:
    print (f"{k} -> {persona[k]}")


print("\n")
#Favourite Number
people: dict = {"Piero": "", "Paolo": "", "Gianpiero": "", "Gianpaolo": "", "Sirio": ""}
favNums: list = []
for k in people:
    num: int = random.randint(1,100)
    people[k] = num
print(people)
for k in people:
    print (f"{k} -> {people[k]}")

'''

#Glossary
