x = [ 0, 2, 5, 10]
y = [ 0, 3, 5]


def carresgrosselistedistance(x, y):
    xlist = list()
    ylist = list()
    grosse_liste = list()
    print(len(x), len(y))
    for i in range(len(x)):
        try:
            xlist.append(x[i + 1] - x[i])
        except IndexError: 
            xlist.append(x[i])
    for i in range(len(y)):
        try:
            ylist.append(y[i + 1] - y[i])
        except IndexError:
            ylist.append(y[i])
    print(xlist, ylist)
    grosse_liste += xlist + ylist
    grosse_liste = xlist + list(set(ylist) - set(xlist))
    print(grosse_liste)
    """
    sol =0
    for xgrosse in grosse_liste:
        for ygrosse in grosse_liste:
            if xgrosse == ygrosse: 
                sol +=1 
    return sol
    """
    return len(grosse_liste)


def carreslistedescoordonnes(lstx,lsty):
    coordx = list()
    coordy = list()
    for lentx in range(len(lstx)):
        try:
            coordx.append(lstx[lentx])
            coordx.append(lstx[lentx+1])
        except IndexError:
            coordx.append(lstx[lentx])
            #coordx.append(lstx[lentx])
    for lenty in range(len(lsty)):
        try:
            coordy.append(lsty[lenty])
            coordy.append(lsty[lenty+1])
        except IndexError:
            coordy.append(lsty[lenty])
            #coordy.append(lsty[lenty])
    
    return coordx, coordy
