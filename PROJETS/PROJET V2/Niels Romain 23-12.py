def test(x, y):
    sol = 0
    stock = 0
    for elemy in y:
        for elemx1 in x:
            print("elemx1:", elemx1, "elemy:", elemy, "Stock:", stock)
            if elemx1 - stock == elemy or elemx1 == elemy or elemx1 + stock == elemy:
                sol += 1
            print("Solution:", sol)
            stock = elemx1
    return sol


"""
sarix = 0
for i in range(len(x)):
    sarix += i
sariy = 0
for i in range(len(y)):
    sariy += i
    
print("SariY",sariy,"SariX",sarix)
"""
"""
def carres(tablex,tabley):
    Stocky=0
    Stockx=0
    sol = 0
    for arx in tablex:
        for ary in tabley:
            if carrestest(arx,Stockx,Stocky,ary) == True:
                sol += 1
            print("Solution:", sol)
            Stocky = ary
        Stockx = arx
    
def carrestest(arx,stockx,stocky,ary):
    if arx - stockx == ary:
        return True
    if arx - stockx == ary - stocky:
        return True
    if arx - stockx == ary + stocky:
        return True
    if arx + stockx == ary:
        return True
    if arx + stockx == ary - stocky:
        return True
    if arx + stockx == ary + stocky:
        return True
    if arx == ary:
        return True
    
carres(x,y)
"""


def carrestest(arx, stockx, stocky, ary):
    if arx - stockx == ary:
        return True
    if arx - stockx == ary - stocky:
        return True
    if arx - stockx == ary + stocky:
        return True
    if arx + stockx == ary:
        return True
    if arx + stockx == ary - stocky:
        return True
    if arx + stockx == ary + stocky:
        return True
    if arx == ary:
        return True


sol = 0
"""
for ax in x:
    for bx in x:
        for ay in y:
            for by in y:
                if carrestest(ax,bx,by,ay)== True:
                    sol+=1
                    print(sol)
      """


def trouvercarres(x, y):
    sol = 0
    for lentx in x:
        for rapidex in x:
            for lenty in y:
                for rapidey in y:
                    if rapidex - lentx == rapidey - lenty:
                        sol += 1
    return sol


from collections import Counter
