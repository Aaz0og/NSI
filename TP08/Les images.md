# _Travail sur les images_
- [[TP08 - Algorithmique - 3 - rotation.pdf|TP08 Algorithmique - rotation]]
- [[rotation_image.py|Code de rotation d'image naïf]]
- [[rotation_image_récursif.py|Code de rotation d'image récursif]]

Le système de couleurs basique: 
- [R,V,B] <span class="red">Rouge, <span class="green">Vert, <span class="blue">Bleu 
- [0,0,0] Noir
- <span class="red">[255,0,0] Rouge
- [255,255,255] Blanc
- <span class="yellow">[255,255,0] Jaune 

Pour python on peut coder des images avec des listes dans des listes. 
On peut utiliser une bibliothèque qui s'appelle PILLOW / PIL, Python Image Library. 
 
```
Pour toutes les lignes y:
	Pour toutes les collones x:
		Je récupère le pixel en (y,hauteur -x-1) de l'image d'origine 
		Mettre ce pixel en (x,y) de la nouvelle image
```

1. 1. La complexité spaciale de cette algorithme est côté x côté càd le nombre de pixels. La complexité temporelle est de 2x la complexité spaciale. 