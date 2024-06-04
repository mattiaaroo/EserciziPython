import random

hare: str = "H"
tartoise: str = "T"
hare_p: int = 0
tartoise_p: int = 0
hareWins: bool = False
tartoiseWins: bool = False
field: list = []

def createField(field):
    if field:
        field = []
    else:
        for i in range(69):
            field.append("_")

def tartoiseNut(tartoise_p):
    res = random.randint(1, 10)
    if 1 <= res <= 5:
        tartoise_p += 3 
    elif 6 <= res <= 7:
        if tartoise_p < 6:
            tartoise_p = 0 
        else:
            tartoise_p -= 6
    else:
        tartoise_p += 1
    return min(tartoise_p, 69)
        
def hareNut(hare_p):
    res: int = random.randint(1,10)
    if 1 <= res <= 2:
        hare_p = hare_p
    elif 3 <= res <= 4:
        hare_p += 9
    elif res == 5:
        if hare_p < 12:
            hare_p -= hare_p
        else:
            hare_p -= 12
    elif 6 <= res <= 9:
        hare_p += 1
    elif res == 10:
        if hare_p < 2:
            hare_p -= hare_p
        else:
            hare_p -= 2
    return min(hare_p, 69)

turno: int = 0
print("5BANG !!!!! AND THEY'RE OFF !!!!!")
while not hareWins and not tartoiseWins:
    
    tartoise_p: int = tartoiseNut(tartoise_p)
    hare_p: int = hareNut(hare_p)

    createField(field)
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
    else:
        del field[tartoise_p]
        del field[hare_p]
        
        if tartoise in field:
            index_tartoise: int = field.index(tartoise)
            field.remove(tartoise)
            field.insert(index_tartoise, "_")

        if hare in field:
            index_hare: int = field.index(hare)
            field.remove(hare)
            field.insert(index_hare, "_")

        field.insert(tartoise_p, tartoise)
        field.insert(hare_p, hare)

        print(f"\nturno: {turno} \n field: {field}")
        turno += 1
        continue
