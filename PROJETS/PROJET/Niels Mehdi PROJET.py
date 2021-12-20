import turtle
import random


class Balle(turtle.Turtle):
    gravite = -0.05
    energie_sol = 0.95
    energie_mur = 0.8

    def __init__(self, x=0, y=0):
        super().__init__()
        self.hideturtle()
        self.velocite_y = random.randint(-10, 50) / 10
        self.velocite_x = random.randint(-30, 30) / 10
        self.setposition(x, y)
        self.taille = 30
        self.color((random.random(), random.random(), random.random()))
        self.ite = 0

    def dessiner(self):
        self.clear()
        self.dot(self.taille)

    def bouger(self):
        self.velocite_y += self.gravite
        self.sety(self.ycor() + self.velocite_y)
        self.setx(self.xcor() + self.velocite_x)

    def rebond_sol(self, sol_y):
        if self.ycor() < sol_y:
            self.velocite_y = -self.velocite_y * self.energie_sol
            self.sety(sol_y)

    def rebond_mur(self, mur_x):
        if abs(self.xcor()) > mur_x:
            self.velocite_x = -self.velocite_x * self.energie_mur
            sign = self.xcor() / abs(self.xcor())
            self.setx(mur_x * sign)


largeur = 1200
hauteur = 800

window = turtle.Screen()
window.setup(largeur, hauteur)
window.tracer(0)

balls = [Balle() for _ in range(1)]


def add_ball(x, y):
    balls.append(Balle(x, y))


while True:
    for ball in balls:
        ball.dessiner()
        ball.bouger()
        ball.rebond_sol(-hauteur/2)
        ball.rebond_mur(largeur/2)

    window.update()
