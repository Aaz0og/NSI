<center><b><u> Exercice 2</u></b></center>

```mermaid
graph TD;
	E[Entrée]
	S1[Salle 1]
	S2[Salle 2]
	S3[Salle 3 trésor]
	S4[Salle 4]
	S5[Salle 5]
	B[Boss]
	E --> S1 & S2
	S1 --> E & S6
	S2 --> S4
	S4 --> S5
	S5 --> S1 & S2
	S6 --> S3 & B
	B --> E
```
<br>
<center><b><u> Exercice 3</u></b></center>

1.

```mermaid
graph TD
	S1---S2 & S3 & S4
	S2 --- S5 & S6 & S7
	S4 --- S7
	S5 ---S6
```

2.
```mermaid
graph TD
	S1 --> S2 & S3
	S2 --> S5 & S7
	S3 --> S4
	S4 --> S1 & S6
	S5 --> S6 
	S6 --> S2 & S5
	S7 --> S1 & S2
```
<br>
<center><b><u> Exercice 4</u></b></center>

1.
```mermaid
graph LR
	A --- B
	B --- C & H
	D --- C
	E --- A & C
	F --- E & H
	H --- A & G
```

2.
```mermaid
graph LR
	A --> C & D
	B --> D
	C --> A & B
```
<br>
<center><b><u> Exercice 5</u></b></center>

1.
```mermaid
graph TD
	A --- B & C
	B --- D & E
	C --- F & G
```
2. Il me fait penser aux arbres binaires (vu précédéments) [[TP05 - arbres.pdf|TP05 sur les arbres]]

<br>
<center><b><u> Exercice 6</u></b></center>

Algorithme : 
- On retire un sommet de la pile qui deveint "le sommet courant"
	- SommetCourant : C, Contenu pile : []
- On affiche le commet 
	- (C)
- On empile les voisins de C dans la pile **s'ils n'ont pas déjà été colorié** (donc aucun)
	- Contenu pile : []. La pile est vide, on sort donc de la boucle  

#graphG
```mermaid
graph TD
	A --- C & B
	C --- E & D
	B --- F 
	D --- F
```
1. 
Courant | Pile | Colorié | Affiché
:-:|:-:|:-:|:-:
 || A | A |
A| B,C | A,B,C | A
C| B,E,D | A,B,C,E,D | C
D| B,E,F | A,B,C,D,E,F | D
F| B,E |---| F
E| B |---| E 
B| x |---| B
<br>
<center><b><u> Exercice 7</u></b></center>

#graphG 
- On ajoute D à la liste "chemin"
- Chemin : [A,C,D]
- Pour chauqe voison de A, si le voisin n'est pas déjà dans le chemin :
	- **On regarde si il existe un chemin allant du voisin à F** 
	- Si il existe  un chemin, on le retourne
- Si on sort de la boucle, on n'a pas trouvé de chemin, on retire le sommet du Chemin

Appel (Fonction) | Courant | Chemin | Voisins (aléatoire) 
-|:-:|-|-
Chemin(E,B)| E | [E] | C
Chemin(C,B)| C | [E,C] | A,D
Chemin(D,B)| D | [E,C,D] | F
Chemin(F,B)| F | [E,C,D,F] | B
Chemin(B,B)| B | [E,C,D,F,B] | 
