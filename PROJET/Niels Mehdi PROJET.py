import turtle
import random

class Balle(turtle.Turtle):
    gravite = -0.05
    energie_sol = 0.95
    energie_mur = 0.8
    
    def __init__(self, x=0, y=0):
        super().__init__()
        self.hideturtle()
        self.y_velocity = random.randint(-10, 50) / 10
        self.x_velocity = random.randint(-30, 30) / 10
        self.setposition(x, y)
        self.size = int(30)
        self.color((random.random(),random.random(),random.random()))
        self.ite=0
    def draw(self):
        if ball.ite()==1:
            self.pendown()
            self.penup()
        self.dot(self.size)

    def move(self):
        self.y_velocity += self.gravite
        self.sety(self.ycor() + self.y_velocity)
        self.setx(self.xcor() + self.x_velocity)

    def bounce_floor(self, floor_y):
        if self.ycor() < floor_y:
            self.y_velocity = -self.y_velocity * self.energie_sol
            self.sety(floor_y)

    def bounce_walls(self, wall_x):
        if abs(self.xcor()) > wall_x:
            self.x_velocity = -self.x_velocity * self.energie_mur
            sign = self.xcor() / abs(self.xcor())
            self.setx(wall_x * sign)
    def ite(self):
        self.ite+=1
        if self.ite%50==0:
            return 1
        else: 
            return 2
width = 1200
height = 800

window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

balls = [Balle() for _ in range(1)]

def add_ball(x, y):
    balls.append(Balle(x, y))

window.onclick(add_ball)

while True:
    for ball in balls:
        ball.draw()
        ball.move()
        ball.bounce_floor(-height/2)
        ball.bounce_walls(width/2)

    window.update()