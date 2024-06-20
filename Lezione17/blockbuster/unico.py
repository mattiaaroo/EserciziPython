class Film:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def setID(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def getID(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def isEqual(self, otherFilm):
        return self.id == otherFilm.id
    

class Azione(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Azione"
        self.__penale = 3

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, film, days):
        penale = film.getPenale()
        totale_penale = days * penale
        return totale_penale
        
class Commedia(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Commedia"
        self.__penale = 2.5

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, film, days):
        penale = film.getPenale()
        totale_penale = days * penale
        return totale_penale


class Drama(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Drama"
        self.__penale = 3

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, film, days):
        penale = film.getPenale()
        totale_penale = days * penale
        return totale_penale
    

class Noleggio:
    def __init__(self, film_list: list[Film], rented_film: dict = None):
        self.film_list: list[Film] = film_list
        self.rented_film = rented_film if rented_film is not None else {}

    def isAvailable(self, film: Film):
        if film in self.film_list:
            return True
        return False

    def rentAMovie(self, film: Film, clientID):
        if film in self.film_list:
            self.film_list.remove(film)
            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            self.rented_film[clientID].append(film)
            return True
        return False

    def giveBack(self, film: Film, clientID, days):
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            tot = days * film.getPenale()
            return tot
        return None

    def printMovies(self):
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()} -")
        
    def printRentMovies(self, clientID):
        if clientID in self.rented_film:
            for film in self.rented_film[clientID]:
                print(f"{film.getTitle()} - {film.getGenere()} -")
        else:
            print(f"Cliente {clientID} non ha noleggiato nessun film.")