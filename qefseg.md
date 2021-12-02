<u><b>Exercice 5 :</b></u>

<u>idJoueur</u>|<u>idConsole</u>|Année achat|Nom console|Edition console|Cote|Prix cote
:-:|:-:|:-:|-|-|-|:-:
1|1|1995|Super Nes|Classique|Rare|1000
2|2|2013|PS3|Classique|Basique |100
3|5|2012|PS3|Uncharted|Commun|500
3|3|1992|Game Boy|Classique|Commun|500
1|4|1995|Game Boy|Pikachu|Rare|1000

1. Parce qu'une personne / Joueur peut avoir plusieurs consoles donc idJoueur peut se répéter
2. La côte est redondante et le nom de la console aussi, ces deux choses pourraient être dans un autre tableau

Joueurs.csv

<u>idJoueur</u>|<u>idConsole#</u>|Année achat
:-:|:-:|:-:
1|1|1995
2|2|2013
3|5|2012
3|3|1992
1|4|1995

Consoles.csv

<u>idConsole</u>|Nom console|Edition console|Cote#
:-:|:-:|-|-
1|Super Nes|Classique|Rare
2|PS3|Classique|Basique
3|Game Boy|Classique|Commun
4|Game Boy|Pikachu|Rare
5|PS3|Uncharted|Commun

Cotes.csv

<u>Cote</u>|Prix cote
-|-
Rare|1000
Commun|500
Basique|100

6. Trouver les colones qui se répètent et les séparer en trouvant une clé primaire