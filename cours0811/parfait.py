def ListDiviseur(n) -> []:
    res : int = []
    for i in range( 1, n):
        if n % i == 0:
            res += [i]
    return res

def IsParfait(n : int) -> bool:
    listD : [] = ListDiviseur(n)
    total : int = 0
    for d in listD:
        total += d
    
    if n == total:
        return True
    else:
        return False
    
def Start():
    while True:
        n = input("Entrer un entire > 1 :")
        if IsParfait(int(n)):
            print(n, "est parfait.")
        else:
            print(n, "n'est pas parfait.")
    
        if input("entre (n) pour quitter") == "n":
            break
    
Start()
    
    