def Equation(n):
    
    if n % 3 == 0:
        r = (n / 3) * 2 - 3
    else:
        return "Entre invalide"
    
    return "Avec " + str(n) + " on obtien " + str(r)

def Age():
    r = 0
    divBy4 = False
    divBy3 = False
    while (divBy3 == False or divBy4 == False) and r < 100:
        divBy3 = False
        divBy4 = False
        r += 5
        if (r + 1) % 4 == 0:
            divBy4 = True
            
        if (r - 1) % 3 == 0:
            divBy3 = True
            
    if r <= 100:
        return str(r)
    else:
        return "Erreur"

def Bague():
    r = 5
    noFind = True
    while noFind and r < 100:
        r += 2
        if r % 2 == 1 and r % 3 == 1 and r % 4 == 1 and r % 5 == 1 and r % 6 == 1:
            noFind = False
    
    return str(r)

def BagueList():
    c = 5
    toTest = [2,3,4,5,6]
    r = []
    while c <= 100:
        itWork = True
        for t in toTest:
            if c % t != 1:
                itWork = False
                break
        if itWork:
            r.append(c)
        c += 2
    return r
    

def PouleLapin():
    np = 0
    p = 2
    l = 4
    noFind = True
    while noFind:
        nl = 36 - np
        if (nl * 4) + (np * 2) == 118:
            noFind = False
        np += 1
    return str(np)

def PouleLapinList():
    np = 0
    p = 2
    l = 4
    r = []
    while np < 36:
        nl = 36 - np
        if (nl * l) + (np * p) == 118:
            r.append(str(np))
        np += 1
    return r      

def Jour():
    jours = ["lun","mar","Mer", "Jeu", "ven", "sam", "dim"]
    j = -1
    i = 0
    while i < 2022:
        j += 2
        if j > 7:
            j  -= 7
        
        i += 1
    return jours[j]

def Garcon():
    r = 1
    mg = 11
    mf = 12
    noFind = True
    while noFind and r < 28:
        f = 28 - r
        if (mg * r + mf * f) / 28 == 11.25:
            noFind = False
        r += 1
    return str(r)

print(Age())
print(Bague())
print(PouleLapin())
print(Jour())
print(Garcon())
print(Equation(12))

for r in PouleLapinList(): 
    print(r)
    
for r in BagueList(): 
    print(r)