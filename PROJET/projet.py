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

ball = canvas.create_oval(10, 10, 50, 50, fill='green')

# bouger la balle
xspeed = yspeed = 3
t=1
g=10
class test:
    
    def moveBall():

        global xspeed, yspeed
        canvas.move(ball, xspeed, yspeed)

        (leftPos, topPos, rightPos, bottomPos) = canvas.coords(ball)

        if leftPos <= 0 or rightPos >= Largeur:
            xspeed = -xspeed 
        if topPos <= 0 or bottomPos >= Hauteur:
            yspeed = -yspeed

        canvas.after(30, test.moveBall)

canvas.after(30, test.moveBall)

root.mainloop()

    