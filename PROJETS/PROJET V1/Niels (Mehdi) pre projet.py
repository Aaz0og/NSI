import turtle
import random
import time
sc = turtle.Screen()
sc.bgcolor("black")
sc.title("Balle Niels (Mehdi)")
sc.tracer(0)
balls = []
for _ in range(1):
    balls.append(turtle.Turtle())
"""
Je travaille tout seul je n'ai pas eu le temps de travailler ces vacances, Mehdi n'a rien fais il m'a contacté samedi avec une excuse pour ne pas travailler
Et même pas une ligne de code a donner. je voulais vous en parler aujoud'hui mais je n'étais pas la. J'ai tout fais sur turtle mais je le passerais sur tk
c'est juste plus rapide avec turtle. Bonne soirée
"""
couleurs = ["red", "blue", "yellow", "purple", "orange", "white"]
for ball in balls:
    ball.shape("circle")
    ball.color(random.choice(couleurs))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    g = 0.1
    ball.dy = -2
    ball.dx = random.randint(-3, 3)
while True:
    # Boucle True pour le répeter jusqu'à la fin pour l'instant je n'ai pas de meileure technique
    for ball in balls:
        sc.update()
        ball.dy -= g
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        # Toujours pareil mais pour le mur de droite
        if ball.xcor() > 300:
            ball.dx *= -1
        # Pareil que pour le bas mais pour le mur de gauche
        if ball.xcor() < -300:
            ball.dx *= -1
        # Regarde les coordonnées y de la balle et si elle atteinds quelque chose en dessous de -300 (le bas de l'écran) on inverse la vitesse y pour que la balle remonte
        if ball.ycor() < -300:
            ball.dy *= -1

sc.mainloop()
