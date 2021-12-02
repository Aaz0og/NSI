<u><b>Exercice 1 :</b></u>

Joueurs.csv :

<u>Pseudo</u>: str | <u>IP</u>: IPV4 | Date insription: Time | Or: int| Guilde#: str
-- | :--: | :--: | :--: | --
Tharotyl|166.219.88.149|16/11/2017|2113| La communauté de l'anneau
Namashal| 199.154.114.125|03/07/2017|3719|L'armée du Mordor
Rhenalyrr|20.73.30.74|23/08/2017|2327|Les Elyséens
Khaalindaan|11.6.205.144|09/01/2017|4873|L'organisation XIII
Paulorin|235.180.9.184|01/02/2017|4956| L'organisation XIII

Guildes.csv : 

<u>Guilde</u>: str|Classement: int|Reputation: str|Type: str
-|:-:|:-:|:-:
L'armée du Mordor|1|Hostile|Guerriere
La communauté de l'anneau|4|Pacifique|Aventure
L'organisation XIII| 2|Hostile|Scientifique
Les Elyséens|3|Neutre|Guerriere

---
<u><b>Exercice 2 :</b></u>
1. Oui car c'est une clé primaire
2. Non c'est un integer référencé nulle part autre que R1
3. ~~Oui car c'est une clé étrangère de R1 qui est une clé primaire~~ <span class="green">Faux c'est l'ensemble a-e qui est distinct</span>
4. Non parce que c'est l'ensemble de a et e qui est unique donc ils peuvent se répéter tant que l'ensemble est unique
5. Non parce que a dans R2 est une clé étrangère 
6. Oui car R2 n'est pas référencé dans R1

---

**_SKIP EXERCICE 3, SUR FEUILLE_**

---
<u><b>Exercice 4 :</b></u>
1.2.3.5.6
**Joueurs**( <u>login</u>: str, mot_de_passe: str, idFaction#: int )
**Factions**( <u>idFactions</u>: int, nom_faction: str )
**Peuples**( <u>idPeuple</u>: int, nom_peuple: str )
**Reputation**( <u>login#</u>: str, <u>idPeuple#</u>: int, reputation: int / float )
**Item**( <u>idItem</u>: int, nom_item: str )
**Vente**( <u>idPeuple#</u>: int, <u>idItem#</u>: int, Prix: float, Reputation_min: float )

4. Il ne change pas


---
<u><b>Exercice 5 :</b></u>

<u>idJoueur</u>|<u>idConsole</u>|Année achat|Nom console|Edition console|Cote|Prix cote
:-:|:-:|:-:|-|-|-|:-:
1|1|1995|Super Nes|Classique|Rare|1000
2|2|2013|PS3|Classique|Basique |100
3|5|2012|PS3|Uncharted|Commun|500
3|3|1992|Game Boy|Classique|Commun|500
1|4|1995|Game Boy|Pikachu|Rare|1000

1. Parce qu'une personne / Joueur peut avoir plusieurs consoles donc idJoueur peut se répéter
2. La côte est redondante et le nom de la console auss, ces deux choses pourraient être dans un autre tableau

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