Fichier qui utilise le tri sélectif et le tri par insertion dans: [[ImplementationComplexite.py]]

TP qui l'utilise [[TP6 - Algorithmique - 1.pdf]]

# Les algorithmes de tri
 
8) 1. A chaque entrée dans la boucle sur i, les i premiers éléments de la liste sont triés (ce sont les plus petits)
9) *Avant de rentrer dans la première boucle sur i, 0 éléments sont triés
On suppose que les i-1er éléments sont triés avant de rentrer dnas la (i+1)ème*
La boucle sur i trouve le minimum de la partie non triée 
Le minimum est plus grand que les i-1er éléments.
Sa place est donc en i+1.
Et les i premiers éléments sont triés. 

## Tri par insertion
7) Tri en place, espace constant, grand taux de 1 même si espace n utilisé. La complexité spaciale c'est la longueur de la liste
8) 1. Les i premiers éléments de la liste sont triés après la ième boucle for. 
	2. Si i=0, pas de partie triée, OK
	On suppose que les ier éléments sont triés 
	On doit montrer que les i+1 premiers seront triés après la i+1ème boucle
1) Cas problématique nécessitent une preuve pour la terminaison 
	- while
	- récursivité
Ici, on a 1 while:  
	- i entier, 
	- i diminue à chaque boucle
	- donc i deviendra <= 0 à un moment -> sortie de boucle **While** car (i>0 et m<A[i-1]) 

