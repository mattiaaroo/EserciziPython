class Libro:
    def __init__(self, titolo, autore, stato_prestito):
        self.titolo: str = titolo
        self.autore: str = autore
        self.stato_prestito: bool = stato_prestito
        self.stato_prestito: bool = False

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo: dict[str:bool] = {}
        pass

    def aggiungi_libro(self, libro: Libro):
        self.catalogo[libro] = False

    def presta_libro(self, titolo):
        for l in self.catalogo:
            if l.titolo == titolo:
                if l.stato_prestito:
                    return f'{l} è già in prestito'
                else:
                    l.stato_prestito = True
                    return f'{l} da questo momento è in prestito'
            
    def restituisci_libro(self, libro):
        for l in self.catalogo:
            if l == libro.titolo:
                if l.stato_prestito:
                    l.stato_prestito = False
                    return f'{l} appena restitutito'
                else:
                    return f'{l} non attualmente in prestito'
            
    def mostra_libri_disponibili(self):
        res: list = []
        for libro in self.catalogo:
            if libro.stato_prestito:
                res.append(libro)
        if res:
            return f'nessun libro disponibile attualmente'
        else:
            return res 