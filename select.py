tab = [5,6,8,4,0]
# wybieranie ( selection )

for x in range(len(tab)):
    index = x
    for y in range(x+1, len(tab)):
        if tab[y] < tab[index]:
            index = y
            
    temp = tab[x]
    tab[x] = tab[index]
    tab[index] = temp

print(tab)