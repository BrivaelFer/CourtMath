import random;

def IsAMultiple(mul:int, div:int) -> bool:
    if mul % div == 0:
        return True
    else:
        return False
    
def HaveAMult(lastNb:int, max:int) -> bool:
    for i in range(lastNb, max + 1):
        if IsAMultiple(i, lastNb):
            return True
    return False
def HaveADiv(lastNb:int) -> bool:
    for i in range(1, lastNb + 1):
        if IsAMultiple(lastNb):
            return True
    return False

def PlayerTourn(lastNb:int, player:str, nbsPlay:[])-> int:
    while True:
        nbPlay:int = int(input("Entre un entier :"))
        if nbPlay in nbsPlay:
            print("Nombre déjà jouer.")
        elif IsAMultiple(nbPlay, lastNb) or IsAMultiple(lastNb, nbPlay):
            return nbPlay
        else:
            print("Nombre invalide.")

def Multiple(nb:int, max:int)->[]:
    res = []
    i = 2
    while True:
        m = [nb * i]
        if m < max: return res
        res += m

def Divisers(nb:int)->[]:
    res = []
    i = 1
    while True:
        i += 1
        if nb % i == 0:
            m = [nb / i]
            if m < nb / 2: return res
            res += m

def IATourn(lastNb:int, nbsPlay:[])-> int:
    p = Divisers(lastNb) + Multiple(lastNb)
    for nb in nbsPlay:
        if nb in p:
            p.remove(nb)
    return p[random.randint(0,len(p) - 1)]
