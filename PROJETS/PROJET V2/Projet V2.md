	x= table
	y= table
	fonction jeu(table):
		pour tout les elements dans x:
			trouver système pour se déplacer sur l'axe x
			pour tout les elements dans y:
				liste d'opérations pour voir si la valeur stocké ou actuelle est pareille
				que celle actuelle, et comparer ça a la liste x:
					si c'est vrai ajouter 1 a une variable 
				stocker dans une table la valeur de y actuelle
			
	
Je pense que la complexité augmente par rapport au nombre d'éléments qu'il y a dans la liste. Du moins c'est ce que je pense avec mon algorithme actuel.

\- Niels, Romain

```py
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
```
Voici l'algrorithme principal que nous avons avec Romain, il ne marche pas mais il y  a moyen d'avoir quelque chose nous pensons. (Le fichier py que je vous ai envoyé contient plusieurs algorithme globalement le même mais aucun ne marche).