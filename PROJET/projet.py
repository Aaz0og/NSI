from tkinter import *
# Taille de l'écran
Largeur = 800
Hauteur = 600
# Fenêtre Tkinter
root = Tk()
canvas=Canvas(root,width=Largeur,height=Hauteur,background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# width fixe l'épaisseur du trait
# outline donne la couleur de celui-ci
# fill est la couleur de remplissage

class balle:
    def mouvement(self):
        pass    
    def gravite(self):
        pass
        gravite = 10
    def rebord(self):
        pass
    def afficher(self,image):
        pass
    def __init__(self,y,x,ecran,taille_ecran,taille_balle,temps_collision):
        r=30
        l,h = (300,200)
        self.x = x
        self.y = y
        self.ecran = ecran
        self.taille_ecran=taille_balle
        self.taille_balle=taille_ecran
        self.temps_collision=temps_collision
        self.balle = canvas.create_oval(l-r,h-r,l+r,h+r,width=1, outline="red",fill='blue')
    
bille=balle.balle
canvas.create_oval(bille)

root.mainloop()

    