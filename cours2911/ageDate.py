def nDay(j: int, m: int)-> int:
    r = j
    jm = [
        31,29,31,30,
        31,30,31,31,
        30,31,30,31
    ]
    for i in range(m - 1):
        r += jm[i]
    return r

def JourSemaine(nbD: int)-> str:
    js = [
        "lundi",
        "mardi",
        "mercredi",
        "jeudi",
        "vendredi",
        "samedi",
        "dimanche"
    ]
    return js[(nbD % 7) - 1]

j = input("Entre le jour entre (1 - 31):")
m = input("Entre le mois entre (1 - 12):")
print("On est " + JourSemaine(nDay(int(j),int(m))) + " !")    