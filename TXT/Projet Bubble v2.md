Projet bubble v2

class balle:
	"Regroupement de toutes les fonctions qui s'occupent de la balle"
	def gravite(self):
		"Soccupe de la gravité de la balle"
	def mouvement(self):
		"Fais bouger la balle a travers l'écran"
	def rebond(self):
		"Fais rebondir la balle si elle entre en contact avec les murs et le sol, pas besoin d'une class/fonction terrain car on va utiliser les bords de la fenêtre"
	def __init__(self,position_ecran,taille_ecran,taille_balle,temps_collision):