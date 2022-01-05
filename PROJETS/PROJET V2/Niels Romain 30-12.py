x = [0, 3, 6, 9]
y = [0, 3, 6, 9]


def carrestestcomplique(x, y):
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


print(carrestestcomplique(x, y))
