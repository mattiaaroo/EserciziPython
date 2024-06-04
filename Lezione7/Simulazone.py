import random

hare: str = 'H'
tartoise: str = 'T'
hare_p: int = 0
tartoise_p: int = 0
hareWins: bool = False
tartoiseWins: bool = False
field: list = []

def fieldBuilding(field):
    field.append(["_"] * 70)
    return field
    

def hareNut(hare_p, hareWins):
    res: int = random.randint(1, 10)
    if 1 <= res <= 5:
        hare_p += 3
    elif 6 <= res <= 7:
        if hare_p < 6:
            hare_p = 0
        else:
            hare_p -= 6
    else:
        hare_p += 1
    if hare_p >= 70:
        hare_p == True
    else:
        return hare_p

def tartoiseNut(tartoise_p, tartoiseWins):
    res: int = random.randint(1,10)
    if 1 <= res <= 2:
        tartoise_p = tartoise_p
    elif 3 <= res <= 4:
        tartoise_p += 9
    elif res == 5:
        if tartoise_p < 12:
            tartoise_p = 0
        else:
            tartoise_p -= 12
    elif 6 <= res <= 9:
        tartoise_p += 1
    elif res == 10:
        if tartoise_p < 2:
            tartoise_p = 0
        else:
            tartoise_p -= 2
        
    if tartoise_p >= 70:
        tartoiseWins == True
    else:
        return tartoise_p

def turno(field, hare_p, tartoise_p):
    field = fieldBuilding(field)
    tartoise_p = tartoiseNut(tartoise_p, tartoiseWins)
    hare_p = hareNut(hare_p, hareWins)
    if hare_p == tartoise_p:
        field[hare_p] = "OUCH!"
    else:
        field[tartoise_p] = tartoise
        field[hare_p] = hare
    return field, hare_p, tartoise_p

field = fieldBuilding(field)

while not hareWins and not tartoiseWins:
    field, hare_p, tartoise_p = turno(field, hare_p, tartoise_p)
    print(field)

    if hare_p >= 69:
        hareWins = True
        print("HARE WINS || YUCH!!!")
    elif tartoise_p >= 69:
        tartoiseWins = True
        print("TORTOISE WINS! || VAY!!!")
    elif hare_p == tartoise_p:
        print("OUCH!!!")


