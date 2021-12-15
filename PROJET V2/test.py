x = [0,  3, 6, 9]
y = [0,  3, 6, 9]


def test(x, y):
    sol = 0
    stock = 0
    while True:
        for elemy in y:
            for elemx1 in x:
                print("elemx1:", elemx1, "elemy:", elemy, "Stock:", stock)
                if elemx1-stock == elemy or elemx1 == elemy:
                    sol += 1
                print("Solution:", sol)
                stock = elemx1
        break
    return sol


print(test(x, y))
