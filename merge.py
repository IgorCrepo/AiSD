
#scalanie (merge)

def SCAL(T ,p ,q ,r):
    lewy = p
    prawy = q + 1
    glowny = p

    K = T.copy()

    while lewy <= q and prawy <= r:
        if K[lewy] <= K[prawy]:
            T[glowny] = K[lewy]
            lewy += 1
        else:
            T[glowny] = K[prawy]
            prawy += 1
        glowny += 1

    while lewy <= q:
        T[glowny] = K[lewy]
        lewy += 1
        glowny += 1

    while prawy <= r:
        T[glowny] = K[prawy]
        prawy += 1
        glowny += 1



T = [8, 4, 6, 0, 1, 4, 13, 99, 0, -12, 4444]


def SC(T, p, r):
    if (p < r):
        q = (p + r) // 2
        SC(T, p, q)
        SC(T, q + 1, r)
        SCAL(T, p, q, r)
    
    return T


print(SC(T, 0, len(T) - 1))

