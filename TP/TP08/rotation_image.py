from PIL import Image

# Ouverture de l'image de base et attribution de ses dimensions a des variables
img = Image.open("./mario.png")
largeur, hauteur = img.size

#Création d'une nouvelle image noire avec les dimensions de l'image de base
nw = Image.new("RGB", (img.size))

# Boucle dans une boucle qui a comme "durée" ne nombre de pixels sur x et y
def rotation():
    #Fait tourner une image dans le sens horaire
    for y_ori in range(largeur):
        for x_ori in range(hauteur):
            # Mettre le pixel de l'image d'origine sur la nouvelle image en se servant des données des boucles
            nw.putpixel((x_ori,y_ori), (img.getpixel((y_ori, hauteur-x_ori-1))))
rotation()

# Affiche notre nouvelle image puis l'enregistre
nw.show()
nw.save("rotation_naïf.png")

# Vérification de la taille d'une image
verif = Image.open("./mario.png")
larg,haut = verif.size


def verification():
    largeur_verif= 128
    hauteur_verif= 128
    assert larg == largeur_verif, "Pas la même largeur"
    assert haut == hauteur_verif, "Pas la même hauteur"

verification()
# Niels Carlon--Mismer