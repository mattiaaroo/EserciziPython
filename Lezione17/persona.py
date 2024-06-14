''' La classe Persona deve avere i seguenti metodi:

    init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, 
    impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, 
    "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; 
    se first_name e last_name non sono due stringhe, allora assegnare None all'età.
    setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. 
    Il valore viene modificato se e solo se viene passata al metodo una stringa. 
    In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
    setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
    setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. 
    Il valore viene modificato se e solo se viene passato al metodo un numero intero. 
    In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
    getName(): consente di ritornare il nome di una persona.
    getLastname(): consente di ritornare il cognome di una persona.
    getAge(): consente di ritornare l'età di una persona.
    greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"

'''

class Persona:
    def __init__(self, first_name, last_name):
        if type(first_name) is str:
            self.__first_name: str = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")
        
        if type(last_name) is str:
            self.__last_name: str = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")
        
        if self.__first_name != None and self.__last_name != None:
            self.__age: int = 0
        else:
            self.__age = None


    def setname(self, first_name):
        if type(first_name) is str:
            self.__first_name: str = first_name
        else:
            return "Il nome inserito non è una stringa!"

    def setLastName(self, last_name):
        if type(last_name) is str:
            self.__last_name: str = last_name
        else:
            return "Il cognome inserito non è una stringa!"

    def setAge(self, age):
        if type(age) is int:
            self.__age: int = age
        else:
            return "L'età deve essere un numero intero!"

    def getName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    
    def greet(self): 
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")


mattia = Persona("mattia", "ro")
print(mattia.greet())


