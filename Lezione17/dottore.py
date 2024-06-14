'''
    costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel). 
    Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, 
    altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, 
    ad esempio, "La parcella inserita non è un float!".
    setSpecialization(specialization): consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. 
    Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stamapre un messaggio di errore, 
    ad esempio "La specializzazione inserita non è una stringa!".
    setParcel(parcel): consente di impostare la parcella di un dottore, modificando il valore del relativo attributo. 
    Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario, stamapre un messaggio di errore, 
    ad esempio "La parcella inserita non è un float!".
    getSpecialization(): consente di ritornare la specializzazione del dottore.
    getParcel(): consente di ritornare la parcella del dottore.
    isAValidDoctor(): stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, 
    in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!", 
    se il dottore risulta valido. In caso contrario, stampare "Doctor nome e cognome is not valid!".
    doctorGreet():tale metodo richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto "Sono un medico {specializzazione}"

'''
from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization, parcel):
        super().__init__(first_name, last_name)
        self.__specialization = specialization
        self.__parcel = parcel

        if type(specialization) is str:
            self.__specialization: str = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
        if type(parcel) is float:
            self.__parcel: float = parcel
        else:
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization):
        if type(specialization) is float:
            self.__specialization: float = specialization
        else:
            print("La parcella inserita non è un float!")
            
    def setParcel(self, parcel):
        if type(parcel) is float:
            self.__parcel: float = parcel
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.getAge() >= 30:
            return "Doctor nome e cognome is valid!"
        else:
            return "Doctor nome e cognome is not valid!"
        
    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.__specialization}")


dottore1 = Dottore("mattia", "ro", "fegatite", 104.4)
dottore1.doctorGreet()