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
        print("Jet " + str(i + 1) + " : " + str(n))
        i += 1
        
    return t

def State(tirage):
    
    for i, nv in enumerate(tirage):
        x = ""
        for j in range(nv - 1):
            x += "X"
        print(str(i + 1) + "|" +x)
        

State(Tirage(8, 20))