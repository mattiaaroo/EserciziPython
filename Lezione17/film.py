'''- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
'''

class Film:
    def __init__(self, id, film):
        self.id = id
        self.film = film

    def setID(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def getID(self):
        return self.id
    
    def getTtile(self):
        return self.title
    
    def isEqual(self, otherFilm):
        return self.id == otherFilm.id
    
    