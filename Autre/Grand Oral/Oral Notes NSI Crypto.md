# La crypto (meilleur sujet)

En tout cas pour les bitcoins, ils sont stocké a aucun endroits spécifiques, ils sont simplement une inscription dans la blockchain (grand registre des transactions) donc on peut recevoir des bitcoins mêmes si notre portefeuille est éteint ou même si on n'a pas de portefeuille, il faut simplement un couple de clés cryptographiques pour y accéder, un logiciel n'est nécessaire que si l'ont veut dépenser ces bitcoins 

- Une clé privée est un nombre aléatoire de 256 bits (32 octets).

- La clé privée est encodée, de façon à en condenser l’écriture, sur 51 caractères (en commençant par un 5) et peut être représentée sous forme de QR code :![[nb-de-cles-privees-bitcoin-51caracteres.jpg]]

- L’encodage en _base58check_ comprend un système de somme de contrôle pour éviter les erreurs de saisie.

- Il existe 2 puissance 256 possibilités de clés privées différentes, soit 1,16 X 10 puissance 77, c’est à dire plus que le nombre d’atomes dans la galaxie (estimé à 10 puissance 68). Il est donc totalement improbable de générer deux fois de façon aléatoire la même clé privée. Ainsi on peut en toute sécurité générer une nouvelle clé (à condition de le faire de façon aléatoire) sans avoir à vérifier si cette dernière est ou non déjà utilisée.
	Pour la même raison, générer et de tester un grand nombre de clés privées aléatoires dans l’espoir de tomber sur un compte contenant des bitcoins est totalement vain.

- La fabrication d’une clé privée ne nécessite donc pas la vérification et l’enregistrement sur le réseau, ce qui permet à Bitcoin de fonctionner de façon décentralisée.
  On calcule la clé publique à partir de la clé privée. <mark style="background: #FF5582A6;">L’inverse est évidemment impossible.</mark> 
  
 La **Blockchain**:
 - Développé à partir de 2008 au début juste une technologie de transfert de données, elle offre de hauts standars car elle fonctionne sans organe central de contrôle et donc elle offre transparence et sécurité
 - La Blockchain permet aux utilisateurs connectés au réseau de partager des données sans intermédiaire
 - à finir https://www.economie.gouv.fr/entreprises/blockchain-definition-avantage-utilisation-application

Les problèmes de la Blockchain :
- [Lien 1](https://bitcoin.fr/ne-nions-pas-le-probleme-electrique-du-bitcoin/)
- [Lien 2](https://www.clubic.com/bitcoin/actualite-368887-les-grosses-pannes-electriques-en-chine-affectent-le-bitcoin.html)
- [Lien 3](https://www.franceculture.fr/emissions/la-revue-de-presse-internationale/la-revue-de-presse-internationale-du-mercredi-26-janvier-2022)

## Le taux de hachage s'écroule

D'importantes fermes de minage établies en Chine se sont retrouvées sans courant pour poursuivre leur activité. Et sans elles, on a très rapidement constaté que le taux de hachage s'est écroulé sur les [plateformes crypto](https://www.clubic.com/antivirus-securite-informatique/cryptage-cryptographie/crypto-monnaie/article-877095-1-comparatif-plateformes-crypto-meilleur-service-acheter-vendre-cryptomonnaies-8201.html) .
En 24 heures, le taux de hachage a chuté de 20 % sur Binance Pool, de 24,5 % sur Antpool, de 18,9 % sur BTC.com et de 33% sur Poolin.

Pour rappel, le taux de hachage quantifie la vitesse à laquelle un réseau est capable de calculer une fonction de hachage. La résolution d'une multitude de ces fonctions est nécessaire pour sécuriser les échanges et les enregistrer dans le registre de la [blockchain](https://www.clubic.com/antivirus-securite-informatique/cryptage-cryptographie/crypto-monnaie/dossier-20215-guide-crypto-tout-comprendre-a-la-blockchain.html) . Plus de mineurs sont disponibles, plus le taux de hachage est élevé, plus le réseau est en mesure de résoudre les opérations.
Donc notre argent peut chuter si des ordinateurs ne sont pas en ligne, le bitcoin comme ça n'a pas l'air sûr
Le minage des cryptomonnaies utilisent énormément d'électricité, les fermes vont a l'endroit ou le courant est le moins cher et en prennent un max ce qui fait monter le prix et donc partout le courant a un prix élevé alors qu'elle pourrait ne pas coûter très cher 
[Attaque Sybil](https://fr.wikipedia.org/wiki/Attaque_Sybil) 
[Consommation d'électricité minage](https://www.lesechos.fr/finance-marches/marches-financiers/lesma-sinquiete-dune-methode-energivore-de-minage-du-bitcoin-1380331#:~:text=Le%20minage%20des%20cryptos%20repr%C3%A9senterait,d'enjeu%20%C2%BB%20en%20juin. )

# Les questions possibles: 

- **Qu'est ce qu'un bit / octet** 
	- C'est une traduction de Binary digit, en français : Chiffre Binaire (donc 0 ou 1)
- **Pourquoi un URL de wallet commence par 5 ?** 
	- C'est simplement comme ça ?
- **Qu'est ce qu'un encodage**
	- <mark style="background: #FF5582A6;">Trouver une réponse</mark> 
- **Somme de contrôle ?** 
	- C'est comme si on voulait vérifier une grosse informations rapidement, imaginons que la question est donner tout les 100 premiers nombres entiers donc de 0 a 100, on va tout d'abord préparer une somme de contrôle pour la correction, on va additioner tout les nombres de 0 a 100 sans aucune faute, et ensuite pour vérifier si une personne a répondu correctement on va simplement additionner tout ses chiffres et si c'est différent de ce que nous avons calculé au préalable il a fait une faute (expliqué comme ça il y a une chance que ça passe par exemple si la personne ajoute a un nombre et enlève a un autre mais quand on est dans le monde de l'informatique on ne peut pas puisque les chiffres qu'on utilise sont tiré du code ascii du texte entré)
- **Qu'est ce qu'un organe de sécurité ?**
	- ***Je ne pense pas que cette question sera posée*** et je n'ai pas de quoi répondre
- **Sans intermédiaire ? Donner un / des exemple d'intermédiaires** 
	- Exemple le plus simple, une banque, quand on fait une transaction la banque est l'intermédiaire, c'est elle qui gère notre transaction elle peut très bien dire non si elle le veut et peut aussi rediriger la transaction vers ou bon lui semble
- **C'est quoi le hachage ?** 
	- [Qu'est ce que le hachage](https://culture-informatique.net/cest-quoi-hachage/) 
	[Hashage crypto](https://cryptoast.fr/hash-hachage-bitcoin-blockchain/)
	De ce que je sais je peux dire que c'est quand on va prendre en entrée des données et on va en sorte les crypter, on va créer une empreinte avec une système de hash, par exemple 123 va devenir 132c2dr2409g (pas la vraie chose mais en gros c'est ça, c'est aussi beaucoup plus long)