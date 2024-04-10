def cal1(num:int):
    if num % 3 == 0 and num >= 0 and num <= 100:
        res = num // 3
        res *= 2
        res -= 3
        print(num, res)

for i in range(100):
    cal1(i) 
    
print("_______")

def test(num:int):
    if num % 5 == 0 and (num - 1) % 3 == 0 and (num + 1) % 4 == 0:
        return True
    return False

def ageAlice()->int:
    for i in range(101):
        if test(i):
            print(i)
    

ageAlice()

print("_______")

def testBague(num:int)->bool:
    for i in range(2, 7):
        if num % i != 1: return False
    return True

def bagueNun():
    for i in range(1, 101):
        if testBague(i): print(i)
        
bagueNun()

def pouleLapin(h:int, p:int):
    poule = 1
    while poule <= h:
        lap = 0
        while lap <= h - poule:
            if (poule * 2) + (lap * 4) == p and poule + lap == h: print('poule:' + str(poule) +' lapin:' + str(lap))
            lap += 1
        poule += 1

pouleLapin(36, 118)