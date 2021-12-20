x = [ 0, 2, 5, 10]
y = [ 0, 3, 5]

"""
def test(x, y):
    sol = 0
    stock = 0
    for elemy in y:
        for elemx1 in x:
            print("elemx1:", elemx1, "elemy:", elemy, "Stock:", stock)
            if elemx1-stock == elemy or elemx1 == elemy or elemx1 + stock == elemy:
                sol += 1
            print("Solution:", sol)
            stock = elemx1
    return sol
"""
def test(x,y):
    pass

#print(test(x, y))
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