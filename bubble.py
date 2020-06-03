# bąbelkowe(bubble)
tab = [-23, 6,9, 0, -24, 56, 127, 9, 4, 11, 0 , -2]
for x in range(len(tab) - 1, 0, -1):
    for y in range(x):
        if tab[y] >  tab[y+1]:
            temp = tab[y]
            tab[y] = tab[y+1]
            tab[y+1] = temp

print(tab)

tab = [-6,46,9,11,23]

for x in range(len(tab)-1, 0, -1):
    for y in range(x):
        if tab[y] > tab[y+1]:
            temp = tab[y]
            tab[y] = tab[y+1]
            tab[y+1] = temp
print(tab)

