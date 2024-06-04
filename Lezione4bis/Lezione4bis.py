'''x: list[float]= [1, 2, 3, 4, 5]
y: float = 5
subList: list = []
def substract_all(x ,y):
    for num in x:
        subList.append(num - y)
    return subList
print(subtract_all(x, y))
 
print("\n")
mylist: list[float] = [1,2,3,4,5]
y: list[float] = [2,3,4,5,6]
listaRisultato: list[float] = []
def subtract_lists(mylist, y):
    for i in range(len(mylist)):
            listaRisultato.append(mylist[i] - y[i])
    return listaRisultato
print(subtract_lists(mylist, y))

print("\n")
#s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
s: str = "ciao mondo"
def counter(s):
    listaCounter: list[int] = []
    listaCounter.append = (len(s))
    listaCounter.append = len(str.split())
    parole = s.split()
    paroleDiverse = set(parole)
    listaCounter.append = len(paroleDiverse)
    listaCounter.append = len(s.split('.')) - 1
    return listaCounter
print(counter(s))

#s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
s: str = "ciao come stai. tutto bene. ciao io sto bene"
def word_count(s):
    s = s.replace('.', '').replace('.', '').replace(',', '').replace(':', '').replace(';', '').replace('!', '')
    dictCounter: dict = dict()
    parole = s.split()
    counterParola: int = 0
    listaParole: list = []
    for parola in parole:
        if parola not in listaParole:
            listaParole.append(parola)
            dictCounter[parola] = 1
        else:
            dictCounter[parola] += 1
    print(listaParole)
    nuovoDict: dict = dict()
    for parola in dictCounter:
        if dictCounter[parola] > 1:
            nuovoDict[parola] = dictCounter[parola]
    print(nuovoDict)

        

    return dictCounter
print(word_count(s))
'''

s: str = "ciao come stai?"
s1: str = "amo roma"
def is_palindrome(s):
    s: str = s.lower().replace(' ', '')
    for i in range(len(s)):
        if s[i] == s[(len(s)-1)-i]:
            continue
        else:
            return False
    return True
print(is_palindrome(s1))