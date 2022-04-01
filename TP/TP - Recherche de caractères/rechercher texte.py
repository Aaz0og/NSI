# -- Exercice 1 --
def rechercher_caractere(texte, caractere):
    conf = 0
    for i in range(len(texte)):
        if texte[i] == caractere:
            conf = 1
            return i
    if conf == 0:
        return -1

def test_rechercher_caractere():
    print(rechercher_caractere("Hello world!", "o")) #Affiche 4
    print(rechercher_caractere("Hello world!", "w")) #Affiche 6
    print(rechercher_caractere("Hello world!", "d")) #Affiche 10
    print(rechercher_caractere("Hello world!", "b")) #Affiche -1
# test_rechercher_caractere()

# -- Exercice 2 --
def rechercher_mot(texte, mot):
    conf = 0
    for i in range(len(texte)):
        if mot[0] == texte[i]:
            if mot[1] == texte[i+1]:
                conf = 1
                try:
                    if mot[2] == texte[i+2]:
                        return i
                except IndexError:
                    return i
    if conf == 0 : return -1 
    
def test_rechercher_mot():
    print(rechercher_mot("Hello world!", "lo"))  # Affiche 3
    print(rechercher_mot("Hello world!", "world"))  # Affiche 6
    print(rechercher_mot("Hello world!", "or"))  # Affiche 7
    print(rechercher_mot("Hello world!", "banane"))  # Affiche -1
    print(rechercher_mot("CAAGTCGAATTGCATGCCGA", "TGCA"))  # Affiche 10
    print(rechercher_mot("Un algorithme glouton (greedy algorithm en anglais, parfois appelé aussi algorithme gourmand, ou goulu) est un algorithme qui suit le principe de faire, étape par étape, un choix optimum local, dans l'espoir d'obtenir un résultat optimum global. Par exemple, dans le problème du rendu de monnaie (donner une somme avec le moins possible de pièces), l'algorithme consistant à répéter le choix de la pièce de plus grande valeur qui ne dépasse pas la somme restante est un algorithme glouton. Dans les cas où l'algorithme ne fournit pas systématiquement la solution optimale, il est appelé une heuristique gloutonne. L'illustration ci-contre montre un cas où ce principe est mis en échec.", "monnaie"))  # Affiche 288
# test_rechercher_mot()


# -- Exercice 3 --
def generer_table_saut(mot):
    M = len(mot)
    table = {}
    for i in range(M-1):
        table[mot[i]] = M-i-1
    return table

def test_generer_table_saut():
    print(generer_table_saut("hello")) #Affiche {"h": 4, "e": 3, "l": 1}
    print(generer_table_saut("world")) #Affiche {"w": 4, "o": 3, "r": 2, "l" : 1}
    print(generer_table_saut("TGCA")) #Affiche {"T": 3, "G": 2, "C": 1}
    print(generer_table_saut("TCTACA")) #Affiche {"T": 3, "C": 1, "A": 2}
    print(generer_table_saut("lo")) #Affiche {"l": 1}
# test_generer_table_saut()


# -- Exercice 4 --
def trouver_mot(texte, mot):
    table = generer_table_saut(mot)
    M = len(mot)
    i = 0
    while i <= len(texte)-M:
        if texte[i:i+M] == mot:
            return i
        else:
            i += table[texte[i+M]] + 1
    return -1

def tests_trouver_mot():
    print(trouver_mot("Hello world!", "lo"))  # Affiche 3
    print(trouver_mot("Hello world!", "world"))  # Affiche 6
    print(trouver_mot("Hello world!", "or"))  # Affiche 7
    print(trouver_mot("Hello world!", "banane"))  # Affiche -1
    print(trouver_mot("CAAGTCGAATTGCATGCCGA", "TGCA"))  # Affiche 10
    print(trouver_mot("Un algorithme glouton (greedy algorithm en anglais, parfois appelé aussi algorithme gourmand, ou goulu) est un algorithme qui suit le principe de faire, étape par étape, un choix optimum local, dans l'espoir d'obtenir un résultat optimum global. Par exemple, dans le problème du rendu de monnaie (donner une somme avec le moins possible de pièces), l'algorithme consistant à répéter le choix de la pièce de plus grande valeur qui ne dépasse pas la somme restante est un algorithme glouton. Dans les cas où l'algorithme ne fournit pas systématiquement la solution optimale, il est appelé une heuristique gloutonne. L'illustration ci-contre montre un cas où ce principe est mis en échec.", "monnaie"))  # Affiche 288
    
tests_trouver_mot()
