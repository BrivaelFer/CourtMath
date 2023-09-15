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

#print(HexaCovertiseur(input("Entre un nombre hexadecimal : ")))

def DeciToHexa(nomberD):
    resulte = ""
    hexa = "0123456789abcdef"
    while nomberD > 16:
        reste = nomberD % 16
        nomberD = nomberD // 16
        resulte = hexa[reste] + resulte
    
    return hexa[nomberD] + resulte

print(DeciToHexa(3015))
          
    