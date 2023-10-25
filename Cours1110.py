def ListNP(max = 100):
    res = [2]
    n = 3
    while n < max:
        
        if IsPremier(n, res):
            res += [n]
        n += 1
    return res

def Strat2(max = 100):
    res =[True] * (max + 1)
    res[0] = False
    res[1] = False
    for i in range(2, max + 1):
        for j in range(i):
            if res[j]:
                if i % j == 0:
                    res[i] = False
    return res

def Strat3(max = 100):
    res =[True] * (max + 1)
    res[0] = False
    res[1] = False
    for i,v in enumerate(res):
        if v:
            for j in range( i * 2, max + 1, i):
                res[j] = False
        
    return res  
     
def IsPremier(n):
    i = n - n // 2
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True

def IsPremier(n, lp):
    for i, p in enumerate(lp):
        if n % p == 0:
            return False
            
    return True
    
    
def ShowList(l):
    r =""
    for i, n in enumerate(l):
        if i == 0:
            r += str(n)
        else:
            r += ", "+ str(n)
            
        if i % 12 == 0:
            r += "\n"
    print(r)

def ShowList2(l):
    r =""
    for i, n in enumerate(l):
        
        if n:
            r +=  str(i) + ", "
    print(r)
# ShowList(ListNP(20000))
ShowList2(Strat3(20000000))