def fibon(n:int)->list:
    s = [2,1]
    while n > s[0]:
        x = s[0] + s[1]
        s = [x] + s
    return s

def plusGrand(num:int, li:list)->int:
    res = 1
    for i in li:
        if res < i and i <= num: res = i
    return res

def decomp(num:int)->list:
    fib = fibon(num)
    res = []
    sou = num
    while sou > 0:
        pg = plusGrand(sou, fib)
        sou -= pg
        res += [pg]
    return res

def littleSix():
    i = 1
    while True:
        d = decomp(i)
        if(len(d) >= 6):
            print(f"{i} :", d)
            return
        i += 1 

littleSix()