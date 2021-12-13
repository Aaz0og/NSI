x = [ 0,  3, 6, 9]
y = [ 0,  3, 6, 9]

def test(x,y):
    sol = 0
    for nbry in range(y[-1]):
        for nbrx in range(x[-1]):
            if nbrx == nbry:
                sol += 1
    return sol 


print(test(x,y))