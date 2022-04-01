def selection(critere):
    return lambda liste: [element for element in liste if critere(element)]

liste = (0, 3, 5, 10, 15, 45, 1029471259075, 4, 6, 9, 12, 25)
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(sorted(selection(lambda x: x%3==0)(liste)))
# print(sorted(selection(lambda x: x%5==0)(liste)))

def multip(nombres):
    for i in range(2,10):
        print(selection(lambda x: x%i==0)(nombres))

multip(nombres)
