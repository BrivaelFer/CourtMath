import random

def somme(n1, n2):
    r = n1 + n2
    
    return str(n1) + "+"+ str(n2) + "=" + str(r) 

def rollDes(tail):
    print(random.randint(1,tail))
def des():
    a = True  
    while a:
        rollDes(6)
        print("Relancer ? oui/non")
        d = str(input())
        if d == "oui":
            a  = True
        elif d == "non":
            a = False
        else:
            print("Entre incorrecte.")
            print("Fin d'excution.")

def  TableMult():
    a = True
    while a:
        n0 = random.randint(3, 9)
        n1 = random.randint(3, 9)
        res = n0 * n1
        print(str(n0) + "X" + str(n1) + "=")
        b = True
        while b:
            entrer = input()
            if  str(entrer) == str(res):
                print("Correct !")
                b = False
                break
            else:
                print("Incorrest !")
                break
        print("Continuer ? oui/non")
        cont = input()
        if cont == "oui":
            a = True
        elif cont == "non":
            a = False
        else:
            print("Entre incorrect")
            a = False
    print("Fin d'execution")

def TropGP():
    print("Entre un nombre entre 1 et 100")
    c = True
    n = random.randint(1, 100)
    while c:
        enterN = int(input())
        if enterN == n:
            print("Gagner!")
            c = False
        elif enterN < n:
            print("Trop petit.")
        elif enterN > n:
            print("Trop grand.")

def Alumette():
    nAl = random.randint(20, 30)
  
    while nAl >= 0:
        print("Il y a "+ str(nAl) + " alumette(s)")
        choix = True
        
        while choix:
            print("Combien d'allumettes prennez-vous ? 1/2/3")
            pt = int(input())
            
            if pt > 0 & pt < 3:
                print("Vous avez pris " + str(pt) + "alumette(s).")
                nAl -= pt
                choix = False
            else:
                print("entre incorrect")
        
        if nAl <= 0: print("Perdu !")
        
        print("Il y a "+ str(nAl) + " alumette(s)")
        iat = random.randint(1, 3)
        choix = True
        while choix:
            if iat > 1 & nAl - iat <= 0:
                iat -= 1
            else:
                nAl -= iat
                choix = False
                
        print("Votre adversaire tire " + str(iat) + " alumette(s).")
        if nAl <= 0: print("Gagner !")

def ChoixFonction():
    
    print("Selectionner jeu:")
    print("1) Table multipliquation")
    print("2) Grand petit")
    print("3) Alumette")
    
    c = int(input())
    
    if c == 1:
        TableMult()
    elif c == 2:
        TropGP()
    elif c == 3:
        Alumette()

ChoixFonction()
            
            
            
            
    
    