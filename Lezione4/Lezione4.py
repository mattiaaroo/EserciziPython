#def rewrite_dict(d: dict[str, int]) -> dict[str, int]
def rewrite_dict(d):
    somma: int = sum(list(d.values()))
    for key, value in d.items():
        value = value / somma
        d[key] = value
    return d
  
d: dict = {"ciao": 2, "hello": 3}
print(rewrite_dict(d))
a = float (input("Inserisci il primo numero: "))
b = float (input("Inserisci il secondo numero: "))
def substruct(a, b):
    return a - b
print(substruct(a, b))


listaNumeri: list = [1, 2, 3, 4, 5, 6, 7, 8]
contatore = 0
def median(listaNumeri):
     median: list = []
     listaNumeri.sort()
     if len(listaNumeri) % 2 == 0:
         medianPosition: int = (len(listaNumeri)) // 2
         median = (listaNumeri[medianPosition] + listaNumeri[medianPosition-1]) / 2

     else:
         medianPosition: int = len(listaNumeri) // 2
         median.insert(1, listaNumeri[medianPosition])
     return median
print(median(listaNumeri))


lunghezzaLimite: int = int(input("Inserire la lunghzza della lista: "))
posizione: int = 0
l: list = []
while posizione <= (lunghezzaLimite-1):
    elemento: int = int(input(f"Inserisci il numero che va in posizione {posizione}: "))
    l.append(elemento)
    posizione += 1
index: int = int(input("Inserisci la posizione della cifra che non devo prendere in considerazione: "))
contatoreIndex: int = 0
def diff_cum(l, index):
    elem = l.pop(index)
    for numero in l:
        elem -= numero
    return elem
diff_cum(l, index)


'''
 str.upper
 str.lower
 str.removesuffix
 list.remove
 list.insert
 list.append
 list.pop
 list.del
 list.sort
 list.reverse
 len
 '''


