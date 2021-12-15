from tkinter import *
Largeur = 800
Hauteur = 600

root = Tk()

canvas = Canvas(root,width=Largeur,height=Hauteur,background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

r=30 # rayon du cercle
x,y = (300,200) # coordonnées du centre du cercle
canvas.create_oval(x-r,y-r,x+r,y+r,width=1, outline="red",fill='blue')

class Balle():
    def __init__(self,x,y,vx,vy,m):
        x = x
        y=y
        vx=vx
        vy=vy
        m=m
    def deplacement(self):
        

root.mainloop()