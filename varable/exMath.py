def HexaCovertiseur(nExa):
    count = len(nExa) - 1
    resulte = 0
    for exa in nExa:
        try:
            exa = int(exa)
            resulte += exa*(16**count)
        except:
            if exa == "A" or exa == "a":
                resulte += 10*(16**count)
            elif exa == "B" or exa == "b":
                resulte += 11*(16**count)
            elif exa == "C" or exa == "c":
                resulte += 12*(16**count)
            elif exa == "D" or exa == "d":
                resulte += 13*(16**count)
            elif exa == "E" or exa == "e":
                resulte += 14*(16**count)
            elif exa == "F" or exa == "f":
                resulte += 15*(16**count)
            else:
                return "entrer invalide"
        count -= 1
    return resulte

def DeciToHexa(nomberD):
    resulte = ""
    hexa = "0123456789abcdef"
    while nomberD > 16:
        reste = nomberD % 16
        nomberD = nomberD // 16
        resulte = hexa[reste] + resulte
    
    return hexa[nomberD] + resulte

def DeciToBi(num):
    resulte = ""
    bi = "01"
    while num > 0:
        resulte = bi[num % 2] + resulte
        num = num // 2
    
    return resulte

def BiToDeci(numB):
    resulte = 0
    
    count = len(numB) - 1
    for bi in numB:
        if bi in ["0", "1"]:
            if bi == "1":
                resulte += 2 ** count
        else:
            return "Entre invalide"   
        count -= 1
    return resulte

def BiToHexa(numB):
    return DeciToHexa(BiToDeci(numB))

def HexaToBi(numH):
    return DeciToBi(HexaCovertiseur(numH))  
