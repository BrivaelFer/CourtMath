def mult(m1:list , m2:list)->list:
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
        res += [t]
    return res
def showRes(mat:list):
    t:str = ""
    for l in range(len(mat[0])):
        t += "("
        for col in mat:
            t += " " + str(col[l]) + " "
        t += ")\n"
    print(t)
def Main():
    mat1 = []
    l = 0
    done = False
    fistLineSize:int = None
    print("Matrice 1:")
    while not done:
        l += 1
        mat1Ligne = []
        print("ligne " + str(l) + " matrice 1:")
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
    mat2 = []
    done = False
    lineSize:int = 0
    for l in range(fistLineSize):
        if lineSize == 0:
            lineDone = False
            while not lineDone:
                i = input("Entrez le un nombre (s: pour finir la ligne):")
                if i == "s": lineDone = True
                else:
                    try:
                        mat2 += [[float(i)]]
                        lineSize += 1
                    except:
                        print("Vous devez entrer un nombre ou s.")
        else:
            for c in range(lineSize):
                b:bool = False
                while not b:
                    i = input("Entrez le un nombre: ")
                    try:
                        mat2[c] += [float(i)]
                        b = True
                    except:
                        print("Vous devez entrer un nombre.")
    showRes(mult(mat1, mat2))

Main()

