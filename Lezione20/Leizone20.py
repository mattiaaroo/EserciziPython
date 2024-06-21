#GESTIONALE PAGAMENTO
'''
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che 
memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set().
 L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. 
 Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, 
 ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo.
 Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
 Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote 
 da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o
   in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo.
 Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, 
 e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere 
 tutte le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito 
con valori differenti e si invochi dettagliPagamento() per ognuno di essi.'''

class Pagamento:
    def __init__(self):
        pass

    def get(self):
        return self.__importo
    
    def set(self, importo):
        self.__importo = importo

    def dettagliPagamento(self):
        return f"Importo del pagamento: {round(self.__importo, 2)}€"
    

class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()

    def dettagliPagamento(self):
        return f"Importo del pagamento in contanti: {round(self.get(), 2)}€"
    
    def inPezziDa(self):
        importoI = self.get()
        importo = self.get()
        pezzi = {}
        pezzi["banconote da 500€"] = importo // 500
        importo %= 500
        pezzi["banconote da 200€"] = importo // 200
        importo %= 200
        pezzi["banconote da 100€"] = importo // 100
        importo %= 100
        pezzi["banconote da 50€"] = importo // 50
        importo %= 50
        pezzi["banconote da 20€"] = importo // 20
        importo %= 20
        pezzi["banconote da 10€"] = importo // 10
        importo %= 10
        pezzi["banconote da 5€"] = importo // 5
        importo %= 5
        pezzi["monete da 2€"] = importo // 2
        importo %= 2
        pezzi["monete da 1€"] = importo // 1
        importo %= 1
        pezzi["monete da 0.50€"] = importo // 0.50
        importo %= 0.50
        pezzi["monete da 0.20€"] = importo // 0.20
        importo %= 0.20
        pezzi["monete da 0.10€"] = importo // 0.10
        importo %= 0.10
        pezzi["monete da 0.05€"] = importo // 0.05
        importo %= 0.05
        pezzi["monete da 0.02€"] = importo // 0.02
        importo %= 0.02
        pezzi["monete da 0.01€"] = importo / 0.01

        print(f"Importo di {round(importoI, 2)}€ da pagare in contanti con:")
        for k, v in pezzi.items():
            if v > 0:
                print(f"{round(v)} {k}")




class PagamentoCarteDiCredito(Pagamento):
    def __init__(self, nomeTitolare, dataDiScadenza, numeroCarta):
        super().__init__()
        self.nomeTitolare = nomeTitolare
        self.dataDiScadenza = dataDiScadenza
        self.numeroCarta = numeroCarta

    def dettagliPagamento(self):
        return f"Importo del pagamento con carta [{self.numeroCarta} (scad. {self.dataDiScadenza}), intestata a: {self.nomeTitolare}]: {round(self.get(), 2)}€"



'''pagamento1 = PagamentoContanti()
pagamento1.set(1234.56)

pagamento2 = PagamentoContanti()
pagamento2.set(478.95)

pagamento3 = PagamentoCarteDiCredito("Mario Rossi", "30/12", "1234 5678 9101 1121")
pagamento3.set(57.99)

pagamento4 = PagamentoCarteDiCredito("Luigi Bianchi", "01/01", "0000 0000 0000 1003")
pagamento4.set(87.09)

# metodo dettagliPagamento per ognuno degli oggetti
print(pagamento1.dettagliPagamento())
print(pagamento2.dettagliPagamento())
print(pagamento3.dettagliPagamento())
print(pagamento4.dettagliPagamento())

# metodo inPezziDa per PagamentoContanti
print(pagamento1.inPezziDa())
print(pagamento2.inPezziDa())'''




#RENDERING GRAFICO

'''
Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. 
Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma 
e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.
'''

from abc import ABC, abstractmethod
class Forma(ABC):
    def __init__(self, nome):
        self.nome = nome

    def getArea(self):
        pass

    def render(self):
        print(self.getArea())


'''
Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. 
Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
'''

class Quadrato(Forma):
    def __init__(self, nome, lato):
        super().__init__(nome)
        self.nome: str = "Quadrato"
        self.lato: int = lato

    def getArea(self):
        return self.lato ** 2
    
    def render(self):
        line = 0
        col = 0
        for line in range(self.lato):
            if line == self.lato-1:
                print("*" * self.lato)
                break
            
            if line == 0:
                print("*" * self.lato, end = "\n")
                line += 1
            
            elif line < self.lato:
                s: str = ""
                for col in range(self.lato):
                    if col == 0 or col == self.lato -1:
                        s += "*"
                    else:
                        s += " "
                print(f"{s}")
        

# quadrato1 = Quadrato("quadrato1", 7)
# quadrato1.render()





'''
Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, 
ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
'''
class Rettangolo(Forma):
    def __init__(self, nome, base, altezza):
        super().__init__(nome)
        self.nome: str = "Rettangolo"
        self.b: int = base
        self.h: int = altezza

    def getArea(self):
        return self.b * self.h
    
    def render(self):
        line = 0
        for line in range(self.h):
            col = 0
            if line == self.h-1:
                print("*" * self.b)
                break
            
            if line == 0:
                print("*" * self.b, end = "\n")
                line += 1
            
            elif line < self.h:
                s: str = ""
                while col <= self.b:
                    if col == 0 or col == self.b -1:
                        s += "*"
                        col += 1
                    else:
                        s += " "
                        col += 1

                print(f"{s}")




# rettangolo1 = Rettangolo("rettangolo1", 10, 8)
# rettangolo1.render()






'''
Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del trinagolo (per semplicità,
 si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stamapre su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore.
 Il traingolo da stampare deve essere un traingolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print, 
e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

'''

class Triangolo(Forma):
    def __init__(self, nome, lato):
        super().__init__(nome)
        self.nome: str = "Triangolo"
        self.lato: int = lato

    def getArea(self):
        return (self.lato ** 2) / 2
    
    def render(self):
        line = 0
        for line in range(self.lato):
            col = 0
            if line == self.lato-1:
                print("*" * self.lato)
                break
            
            if line == 0:
                print("*" * 1, end = "\n")
                line += 1
            
            elif line < self.lato:
                s: str = ""
                while col <= self.lato:
                    if col == 0 or col == line:
                        s += "*"
                        col += 1
                    else:
                        s += " "
                        col += 1

                print(f"{s}")

triangolo1 = Triangolo("triangolo1", 25)
triangolo1.render()