Utilisation du tri sélectif dans [[ImplementationComplexite.py]]
Tp qui l'utilise [[TP6 - Algorithmique - 1.pdf]]

8-a
A chaque entrée dans la boucle sur i, les i premiers éléments de la liste sont triés (ce sont les plus petits)

8-b 
*Avant de rentrer dans la première boucle sur i, 0 éléments sont triés
On suppose que les i-1er éléments sont triés avant de rentrer dnas la (i+1)ème*
La boucle sur i trouve le minimum de la partie non triée 
Le minimum est plus grand que les i-1er éléments.
Sa place est donc en i+1.
Et les i premiers éléments sont triés. 

~~~
def TriSelection(A):

"""In : liste de nombres A

Out : liste triée par sélection"""

for i in range(len(A)):

# Trouve le minimum

idx_min = i

for o in range(i+1, len(A)):

if A[idx_min] > A[o]:

idx_min = o

# Change le minimum trouvé avec le premier nombre

A[i], A[idx_min] = A[idx_min], A[i]

return A