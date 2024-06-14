'''Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
 '''

from persona import Persona
class Paziente(Persona):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def setIdCode(self, idCode):
        self.idCode: str = idCode

    def getIdCode(self):
        return self.idCode
    
    def pazientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()} \nID: {self.idCode}")
    
paziente1 = Paziente("pazzia", "rozzia")
paziente1.setIdCode("r56")
paziente1.pazientInfo()