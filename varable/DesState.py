import random

def Tirage(tail, nt):
    t = []
    i = 0
    while i < tail:
        t.append(0)
        i += 1
    
    i = 0
    while i < nt:
        n = random.randint(1, tail)
        t[n - 1] += 1
        i += 1
        
    return t

def Grah(tirage):
    
    for i, nv in enumerate(tirage):
        x = ""
        for j in range(nv - 1):
            x += "X"
        print(str(i + 1) + "|" +x)
        
def PourCent(tirage):
    ntl = 0
    for t in tirage:
        ntl += t
    for i, t in enumerate(tirage):
        prc = (t / ntl) * 100
        print("Le resulta " + str(i + 1) + " est sorti sur " 
              + str(prc) + "% des lancer soit " + str(t) + " fois")

#Grah(Tirage(8, 20))
def TirageJeu(tail):
    r = [0]*tail
    
    c = 0
    while HaveZero(r):
        r[random.randint(1,tail)-1] += 1
        c += 1
    return r

def HaveZero(t):
    for i in t:
        if i == 0:
            return True
    return False

def Play():
    j = ["j1", "j2"]
    print("\t|1|2|3|4|5|6|total")
    print("\t---------------------")
    for p in j:
        jt = TirageJeu(6)
        tjt = sum(jt)
        r = p +"\t"
        for f in jt:
            r += "|" + str(f)
        r += "|"+ str(sum(jt))
        print(r)
            
        
        
PourCent(Tirage(6, 800))
Play()