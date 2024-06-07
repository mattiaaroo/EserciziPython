class Media:
    def __init__(self, title, reviews) -> None:
        self.title: str = title
        self.reviews: list[int] = reviews

    def set_title(self, title):
        self.title: str = title

    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto):
        self.reviews.append(voto)

    def getMedia(self):
        summ: int = sum(self.reviews)
        return summ/len(self.reviews)
    
    def getRate(self):
        val_media: float = round(self.getMedia(self), 0)
        if val_media == 1:
            return "Terribile"
        if val_media == 2:
            return "Brutto"
        if val_media == 3:
            return "Normale"
        if val_media == 4:
            return "Bello"
        if val_media == 5:
            return "Grandioso"
        
    def ratePercentage(self, voto):
        votoF: int = self.reviews.count(voto)
        percentage: float = len(self.reviews)/votoF * 100
        return percentage
    
    def recensione(self):
        return f"Titolo del Film: {self.title} \nVoto Medio: {self.getMedia()} \nGiudizio: {self.reviews[self.getMedia()]} \nTerribile: {self.ratePercentage(self, 1)} \nBrutto: {self.ratePercentage(self, 2)} \nNormale: {self.ratePercentage(self, 3)} \nBello: {self.ratePercentage(self, 4)} \nGrandioso: {self.ratePercentage(self, 5)}"
    

# Creazione dei due oggetti Media
film1 = Media("Film1", [])
film2 = Media("Film2", [])

# Aggiunta di almeno 10 valutazioni a ciascun film
valutazioni_film1 = [4, 5, 3, 4, 4, 5, 3, 4, 5, 4]
valutazioni_film2 = [2, 3, 2, 1, 2, 3, 1, 1, 2, 2]

for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)

for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

# Richiamo del metodo recensione per ciascun film
print("Recensione Film 1:")
film1.recensione()

print("\nRecensione Film 2:")
film2.recensione()