def ProdMatrice(m1, m2):
    if len(m1[0]) != len(m2[0]):
        print("Produit impossible.")
        return 
    res = []
    for i, c in m2:
        resL= []
        for il, l in m1:
            sn = 0
            for ic, n in c:
                sn += n * l[ic]
            resL[il] = sn
        res[i] = resL
        
def MatriceInv(m):
    