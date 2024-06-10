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
        val_media: float = round(self.getMedia(), 0)
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
        if votoF == 0:
            return f'voto: {voto} non presente'
        else:
            percentage: float = len(self.reviews)/votoF * 100
        return percentage
    
    def recensione(self):
        return (
            f"Titolo del Film: {self.title}\n"
            f"Voto Medio: {self.getMedia():.2f}\n"
            f"Giudizio: {self.getRate()}\n"
            f"Terribile: {self.ratePercentage(1):.2f}%\n"
            f"Brutto: {self.ratePercentage(2):.2f}%\n"
            f"Normale: {self.ratePercentage(3):.2f}%\n"
            f"Bello: {self.ratePercentage(4):.2f}%\n"
            f"Grandioso: {self.ratePercentage(5):.2f}%"
        )
    

class Film(Media):
    def __init__(self, title, reviews):
        super().__init__(title, reviews)


film1 = Film("Film 1", [])
film2 = Film("Film 2", [])

# Aggiunta di almeno dieci valutazioni per ciascun film
valutazioni_film1 = [5, 4, 3, 4, 5, 2, 3, 4, 5, 1]
valutazioni_film2 = [2, 3, 4, 2, 2, 3, 4, 3, 2, 1]

for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)

for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

# Richiamo del metodo recensione per ciascun film
print(film1.recensione())
print(film2.recensione())