def ListNP(max = 100):
    res = [2]
    n = 3
    while n < max:
        
        if IsPremier(n, res):
            res += [n]
        n += 1
    return res

# def Strat2(max = 100):
#     res = []
#     i = 2
#     while i <= max:
#         res += [i]
#         i += 1
#     i = 2
#     s = len(res)
#     while i <= s:
#         j = len()
#         while i * <= max
        
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
        if i % 12 == 0:
            r += "\n"
        
        if i == 0:
            r += str(n)
        else:
            r += ", "+ str(n)
    print(r)

ShowList(ListNP(200000))