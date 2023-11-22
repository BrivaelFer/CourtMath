def mois(m : int)-> str:
    listMois = [
        "janvier",
        "février",
        "mars",
        "avril",
        "mai",
        "juin",
        "juillet",
        "août",
        "septembre",
        "octobre",
        "novembre",
        "décembre"]
    return listMois[m % 12]

def annees(m : int)-> int:
    return 2014 + (m // 12)

def s(n : int) -> int:
    r = 2000
    for i in range(n):
        r = r*1.001 + 1 
    return r

def paulHave(salC):
    an = 0
    ms = ""
    r = 0.0
    m = 0
    while r <= salC:
        r = s(m)
        an = annees(m)
        ms = mois(m)
        m+=1
    print(ms, an)

paulHave(3000.0)
    
    

        