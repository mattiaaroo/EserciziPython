#Esercitazione sulle classi
'''
class Film:
    def __init__(self, titolo, durata):
        self.titolo: str = titolo
        self.durata: int = durata

    def __str__(self):
        return f"titolo del film: {self.titolo}, durata: {self.durata}m"

class Sala:
    def __init__(self, numero_sala, titolo_film, posti_totali, posti_prenotati):
        self.numero_sala: int = numero_sala
        self.titolo_film: str = titolo_film
        self.posti_totali: int = posti_totali
        self.posti_prenotati: int = posti_prenotati
        
    def prenota_posti(self, num_posti) -> bool:
        if num_posti <= self.posti_totali - self.posti_prenotati:
            self.posti_prenotati += num_posti
            return f"prenotazione andata a buon fine"
        else:
            return f"il numero di posti selezionato non è più disponibile"
    
    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati
    
    def __str__(self):
        return f"-sala numero: {self.numero_sala}, film: {self.titolo_film}, posti ancora disponibili: {self.posti_disponibili()}-"

class Cinema:
    def __init__(self) -> None:
        self.sale_cinema: list = []

    def aggiungi_sala(self, sala: Sala):
        if sala not in self.sale_cinema:
            self.sale_cinema.append(sala)

    def prenota_film(self, titolo_film, num_posti):
        for sala in self.sale_cinema:
            if sala.titolo_film == titolo_film:
                sala.prenota_posti(num_posti)

    def __str__(self):
        for sala in self.sale_cinema:
            res: str = (f"-sala numero: {sala.numero_sala}, film: {sala.titolo_film}, posti ancora disponibili: {sala.posti_disponibili()}-")
        return res
        
cinema1 = Cinema()
sala1 = Sala(1, "Divergent", 50, 0)
sala2 = Sala(2, "Me contro Te", 20, 0)
cinema1.aggiungi_sala(sala1)
cinema1.aggiungi_sala(sala2)
print(sala2)
cinema1.prenota_film("Divergent", 5)
cinema1.prenota_film("Me contro Te", 2)
print(sala1)

print(cinema1)
'''


class Prodotto:
    def __init__(self, nome_prodotto, quantità) -> None:
        self.nome_prodotto: str = nome_prodotto
        self.quantità: int = quantità

    def __str__(self):
        return f'prodotto: {self.nome_prodotto} -> quantità: {self.quantità}'


class Magazzino:
    def __init__(self) -> None:
        self.prodotti: dict = {}
        
    def aggiungi_prodotto(self, prodotto: Prodotto):
        nome_prodotto = prodotto.nome_prodotto
        if nome_prodotto not in self.prodotti:
            self.prodotti[nome_prodotto] = prodotto.quantità
        else:
            return f'{prodotto} already in prodotti'

    def cerca_prodotto(self, prodotto: Prodotto):
        if prodotto not in self.prodotti:
            print(f'{prodotto} not in prodotti')
        else:
            print(f'{prodotto}')
        
    def __str__(self):
        for prodotto in self.prodotti:
            res: str = (f'{self.prodotti}')
        return res
    
prodotto1 = Prodotto('mela', 5)
prodotto2 = Prodotto('rum', 9)
magazzino1 = Magazzino()
magazzino1.aggiungi_prodotto(prodotto1)
magazzino1.aggiungi_prodotto(prodotto2)
magazzino1.cerca_prodotto("mela")
print(magazzino1.prodotti)