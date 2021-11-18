# *Le tri fusion*
 
 [[TP7 - Algorithmique - 2.pdf|TP07 Algorithmique - 2]]
[[Tri fusion.py|Fichier Python du tri fusion]]
%%Tri-Fusion entier dans le code%%
 1) 1) 
	 1) L'algorithme s'arrête pour
	 2) n est un entier positif, n diminue a chaque appel récursif, le cas de base est n = 0 donc l'algorithme se termine  
5. La complexité du Tri-Fusion est O(n logn) avec n la longueur de la liste: n logn  est beaucoup plus rapide que n2
6. Au pire la complexité spaciale Nlog2(N)

n | n log2n | n2 | log2n | n
--- | --- | --- |---|---
1000 | 1000x10=10000 | 1000000=10^6|10|1000
100000 | 1000000x20 =20000000 (20 millions) | 10^12 (mille milliard)|20|1000000

n log2n est la meilleure complexité pour un tri
Le tri a bulle a aussi une complexité en n logn, mais il a une complexité dans le pire des cas en n^2 mais la plupart du temps en n logn donc souvent le tri a bulle est le plus préferable. 

#### L'avantage du Tri-Fusion est sa complexité.


