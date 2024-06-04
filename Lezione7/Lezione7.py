'''class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return f'Food({self.name}, {self.price})'

class Menu:
    def __init__(self, foods = []):
        self.foods = foods

    def addFood(self, food: Food):
        self.foods.append(food)
        
    def removeFood(self, food):
        self.foods.remove(food)

    def getAveragePrices(prices):
        return sum(prices) / len(prices)

if __name__ == '__main__':
    margherita = Food("margherita", 5.5, "mozzarella e pomodoro")
    bianca = Food("bianca", 3.5, "olio e sale")
    diavola = Food("diavola", 7, "salame piccante e pomodoro")

    print(diavola)

    menu = Menu()
    menu.addFood(margherita)
    menu.addFood(bianca)
    menu.addFood(diavola)

    print(Menu)


'''
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    pari: list = []
    dispari: list = []
    for n in lista:
        if n % 2 == 0:
            pari.append(n)
        else:
            dispari.append(n)
    allNum: dict = {}
    allNum["pari"] = pari
    allNum["dispari"] = dispari
    return  allNum

print(classifica_numeri([1, 2, 3, 4, 5, 6]))
print(classifica_numeri([]))

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True:
        return "Operazione Permessa"
    elif conditionB & conditionC == True:
        return "Operazione Permessa"
    else: 
        return "Operazione Negata" 
    
print(check_combination(True, False, True))
print(check_combination(False, True, False))

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int, int]) -> list[int]:
    for n, count in da_rimuovere.items():
        contatore = 0
        while contatore < count:
            if n in lista:
                lista.remove(n)
                contatore += 1
            else:
                break
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1})) 

def aggrega_voti(lista_voti: list[dict[str, int]]) -> dict[str, list[int]]:
    votiAggregati = {}
    
    for studente in lista_voti:
        nome = studente['nome']
        voto = studente['voto']
        if nome in votiAggregati:
            votiAggregati[nome].append(voto)
        else:
            votiAggregati[nome] = [voto]
    return votiAggregati

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

print(aggrega_voti([]))

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    pCorretti: dict = {}
    for prodotto in prodotti:
        if prodotti[prodotto] > 20:
            pCorretti[prodotto] = round((prodotti[prodotto])/100 * 90, 1)
    return pCorretti

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 


def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    dictionary : dict = {}
    dictionary["profile"] = name
    dictionary["email"] = email
    dictionary["telefono"] = telefono
    return dictionary


def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    dictionary["profile"] = name  
    if email in input:
        dictionary["email"] = email
    if telefono in input: 
        dictionary["telefono"] = telefono 
    return dictionary

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))