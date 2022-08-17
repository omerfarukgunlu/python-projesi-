# soru 1
def flat(liste):
    yeni_liste = []
    for i in liste:
        if isinstance(i, str) or isinstance(i, int):
            yeni_liste.append(i)
        else:
            for q in i:
                if isinstance(q, str) or isinstance(q, int):
                    yeni_liste.append(q)
                else:   
                    for t in q:
                        if isinstance(t, str) or isinstance(t, int):
                                yeni_liste.append(t)
                        else:
                            for y in t:
                                    if isinstance(y, str) or isinstance(y, int):
                                        yeni_liste.append(y)
       
                                
       
    print(yeni_liste)
        
        
# soru 2

def ters(liste):
    düzenli = []
    for e in liste:
        düzenli.append(e[::-1])
    print(düzenli[::-1])
