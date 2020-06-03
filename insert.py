# wstawianie ( insertion )
tab = [5,6,8,4,0]

for x in range(1, len(tab)):
    obecny = tab[x]
    index = x
    while index > 0 and tab[index-1] > obecny:
        tab[index] = tab[index-1]
        index = index -1
        
    tab[index] = obecny
    
print(tab)