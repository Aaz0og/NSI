from time import perf_counter


def bin(k, n):
    if k == 0 or k == n:
        return 1
    else:
        return bin(k-1, n-1)+bin(k, n-1)


def bin_mem(k, n, mem):
    if (k, n) in mem:
        return mem[(k, n)]
    if k == 0 or k == n:
        mem[(k, n)] = 1
        return 1
    else:
        mem[(k, n)] = bin_mem(k-1, n-1, mem) + bin_mem(k, n-1, mem)
        return mem[(k, n)]


""" 
mem = {}
print(bin_mem(3,5,mem))
print(mem)
"""

memo = {}
n = 25
debut = perf_counter()
for i in range(n):
    for j in range(i+1):
        bin_mem(j, i, memo)

fin = perf_counter()

#print("Temps pour l'exécution", fin-debut, "secondes")

Euro = (500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)


def piecess(pieces, s):
    nb_pieces = 0
    if s == 0:
        return 0
    for elements in pieces:
        if elements <= s:
            nb_pieces += 1
            s -= elements
            print(s)
            piecess(pieces, s)
    return nb_pieces


def rendudynamique(euro,somme):
    pass