import random
import numpy

hare: str = "H"
tartoise: str = "T"
tartoise_stamina: int = 100
hare_stamina: int = 100
hare_p: int = 0
tartoise_p: int = 0
hareWins: bool = False
tartoiseWins: bool = False
field: list[str] = []
meteo: list[str] = ["sun", "rain"]
malus: dict[int:int] = {}
bonus: dict[int:int] = {}
specials: dict[dict:dict] = [malus, bonus]

def createSpecials():
    for _ in range(len(field)):
        if _ % 20 == 0 and _ != 0:
            replace(field, _, "B)")
        elif _ % 15 == 0 and _ != 0:
            replace(field, _, "X")
        else: 
            pass
    for i in range(len(field)):
        if field[i] == "B)":
            bonus[i] = +5
            pass
        if field[i] == "X":
            malus[i] = -5
            pass

def replace(list: list[str], position: int, new_item: str):
    tartoise_p = hare_p = position 
    if new_item == tartoise:
        p: int = tartoise_p
        if list[position] == "B)":
            p += bonus[position]
            if 0 < p < 69:
                tartoise_p = p

        if list[position] == "X":
            p += malus[position]
            if 0 < p < 69:
                tartoise_p = p
                
    if new_item == hare:
        p: int = hare_p
        if list[position] == "B)":
            p += bonus[position]
            if 0 < p < 69:
                tartoise_p = p

        if list[position] == "X":
            p += malus[position]
            if 0 < p < 69:
                tartoise_p = p
    
    if list[position]:
        list.pop(position)
        list.insert(position, new_item)

def createField(field: list[str]):
    createSpecials()
    if field:
        field = []
    else:
        for _ in range(70):
            field.append("_")

def tartoiseNut(tartoise_p: int, tartoise_stamina: int):
    res = random.randint(1, 10)
    stamina_prov: int = tartoise_stamina
    p_prov: int = tartoise_p
    if 1 <= res <= 5:
        p_prov += 3 
        stamina_prov -= 5
    elif 6 <= res <= 7:
        if p_prov < 6:
            p_prov = 0 
        else:
            p_prov -= 6
            stamina_prov -= 10
    else:
        p_prov += 1
        stamina_prov -= 3

    if stamina_prov >= 5:
        tartoise_stamina = stamina_prov
        tartoise_p = p_prov
    else:
        tartoise_stamina = tartoise_stamina
    return min(tartoise_p, 69)
        
def hareNut(hare_p: int, hare_stamina: int):
    res: int = random.randint(1,10)
    stamina_prov: int = hare_stamina
    p_prov: int = hare_p

    if 1 <= res <= 2:
        p_prov = p_prov
        stamina_prov = min(stamina_prov + 10, 100)
    elif 3 <= res <= 4:
        p_prov += 9
        stamina_prov -= 15
    elif res == 5:
        if p_prov < 12:
            p_prov -= p_prov
            stamina_prov -= 20
        else:
            p_prov -= 12
            stamina_prov -= 20
    elif 6 <= res <= 9:
        p_prov += 1
        stamina_prov -= 5

    elif res == 10:
        if p_prov < 2:
            p_prov -= p_prov
            stamina_prov -= 8
        else:
            p_prov -= 2
            stamina_prov -= 8
    if stamina_prov >= 5:
        stamina_prov = stamina_prov
        hare_p = p_prov
    else:
        stamina_prov = stamina_prov
    return min(hare_p, 69)

def getMeteo(meteo):
    newMeteo: str = numpy.random.choice(meteo)
    return newMeteo


print("BANG !!!!! AND THEY'RE OFF !!!!!")
turno: int = 1
meteo_turno = getMeteo(meteo)

while not hareWins and not tartoiseWins:
    tartoise_p: int = tartoiseNut(tartoise_p, tartoise_stamina)
    hare_p: int = hareNut(hare_p, hare_stamina)

    createField(field)

    if turno % 10 == 0:
        i: int = meteo.index(meteo_turno)
        if i == 0:
            newMeteo: str = meteo[1]
            meteo_turno = newMeteo
        else:
            newMeteo: str = meteo[0]
            meteo_turno = newMeteo

    if hareWins and tartoiseWins:
        print("IT'S A TIE")
        break
        
    else: 
        if hare_p == 69:
            hareWins = True
            print("HARE WINS || YUCH!!!")
            break
        elif tartoise_p == 69:
            tartoiseWins = True
            print("TORTOISE WINS! || VAY!!!")
            break
        elif hare_p == tartoise_p and turno > 0:
            print("OUCH!!!")
            continue
            
        else:
            if meteo_turno == "rain":
                tartoise_p = max(tartoise_p - 2, 0)
                hare_p = max(hare_p - 1, 0)

            if tartoise in field:
                index_tartoise: int = field.index(tartoise)
                replace(field, index_tartoise, "_")
            
            if hare in field:
                index_hare: int = field.index(hare)
                replace(field, index_hare, "_")
            
            replace(field, tartoise_p, tartoise)
            replace(field, hare_p, hare)

            print(f"\nturno: {turno} meteo: {meteo_turno} \n field: {field}")
            turno += 1
            continue

print(specials)