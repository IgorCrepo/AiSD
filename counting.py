# zliczanie (counting)
tab = [5,6,8,4,0]
max = max(tab)
tab0 = []
tab_wynik = []

for x in range(max+1):
    tab0.append(0)

for x in range(max+1):
    for y in range(len(tab)):
        if tab[y] == x:
            tab0[x] = tab0[x] + 1
            

for x in range(max+1): 
    for y in range(tab0[x]):
        tab_wynik.append(x)
        
print(tab_wynik)