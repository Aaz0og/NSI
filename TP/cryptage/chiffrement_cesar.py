def cesar():
    mot =input("Quel est le message a crypter ? ").lower()
    cle = int(input("Quel est la cle ? " ))
    if cle > 26: cle %= 26
    tableau = tableau_mkr()
    crypt = str()
    for i in mot:
        crypt += tableau[(tableau.index(i)+cle)%26]
    print("--------")
    print("Le message crypté est : ", crypt)
    print("--------")

def tableau_mkr():
    tableau = list()
    for i in range(26):
        tableau += chr(i+97)
    return tableau

cesar()