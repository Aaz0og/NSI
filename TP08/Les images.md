# _Travail sur les images_
- [[TP08 - Algorithmique - 3 - rotation.pdf|TP08 Algorithmique - rotation]]
- [[rotation_image.py|Code de rotation d'image naïf]]
- [[rotation_image_récursif.py|Code de rotation d'image récursif]]

Le système de couleurs basique: 
- [R,V,B] <span class="red">Rouge</span>, <span class="green">Vert</span>, <span class="blue">Bleu</span> 
- [0,0,0] Noir
- <span class="red">[255,0,0] Rouge</span>
- [255,255,255] Blanc
- <span class="yellow">[255,255,0] Jaune</span>

Pour python on peut coder des images avec des listes dans des listes. 
On peut utiliser une bibliothèque qui s'appelle PILLOW / PIL, Python Image Library. 
 
```
Pour toutes les lignes y:
	Pour toutes les collones x:
		Je récupère le pixel en (y,hauteur -x-1) de l'image d'origine 
		Mettre ce pixel en (x,y) de la nouvelle image
```

1. 1. La complexité spaciale de cette algorithme est côté x côté càd le nombre de pixels. La complexité temporelle est de 2x la complexité spaciale. 

__image.putpixel(coordonnées pixel, valeur du pixel)__

 || Divide and Conquer | Naïf 
- | :-: | :-:
C. Temporelle | n^2 log^2n | n^2
C. Spatiale | 1 |n^2