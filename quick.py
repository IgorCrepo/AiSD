tab = [9,1,2,4,5,7,8,6,3]

def quickSort(lewy, prawy):
    #prawy = len(tab)-1
    
    piwot = tab[prawy]



    x = lewy
    wskaznik = lewy
    while(x < prawy):
        if tab[x] < piwot:
            tab[x], tab[wskaznik] = tab[wskaznik], tab[x]
            wskaznik += 1
        x += 1
    
    tab[prawy] = tab[wskaznik]
    tab[wskaznik] = piwot
    



    if(lewy < wskaznik - 1):
        quickSort(lewy, wskaznik - 1)
    if(wskaznik + 1 < prawy):
        quickSort(wskaznik + 1, prawy)
    
quickSort(0, len(tab)-1)
