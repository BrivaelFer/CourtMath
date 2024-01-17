def mult(m1:[] , m2:[])->[]|None:
    res = []
    for c in m2:
        t = []
        for l in m1:
            if len(c) != len(l): return None
            else:
                n = 0
                for i in range(len(c)):
                    n += c[i] * l[i]
                t += [n]
        res += t
    return res
def showRes(mat:[]):
    t:str = ""
    for l in mat:
        t += "("
        for n in l:
            t += " " + str(n) + " "
        t += ")"
def Main():
    mat1 = []
    l = 1
    done = False
    fistLineSize:int = None
    while not done:
        l += 1
        mat1Ligne = []
        print("ligne" + str(l) + "matrice 1:")
        lineDone = False
        while not lineDone:
            i = input("Entrez le un nombre (s: pour finir la ligne)")
            if i == "s": lineDone = True
            else:
                try:
                    mat1Ligne += [float(i)]
                except:
                    print("Vous devez entrer un nombre ou s.")
        if fistLineSize == None: fistLineSize = len(mat1Ligne)
        mat1 += [mat1Ligne]
        if input("Ajouter une autre ligne(yes/no)? [yes]:") == "no": done = True
        
                
