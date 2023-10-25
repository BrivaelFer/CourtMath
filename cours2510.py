def Syra(n):
    res = []
    while n  not in res:
        res += [n]
        if IsPair(n): n  = n /2
        else : n = (n * 3) + 1
        
    print(res)
 
def IsPair(n):
    if n%2 == 0:return True 
    else:return False
    
for i in range(1,int(input())+1):
    print(i, end=" ")
    Syra(i)