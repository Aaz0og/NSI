import turtle
import random
import time
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Balle")
wn.tracer(0)
balls = []
for _ in range(1):
    balls.append(turtle.Turtle())


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
    
    for ball in balls:
        wn.update()
        ball.dy -= g
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        # mur droite
        if ball.xcor() > 300:
            ball.dx *= -1
        # mur gauche
        if ball.xcor() < -300:
            ball.dx *= -1
        # Regarde si doit rebondir sur sol
        
        if ball.ycor() < -300:
            ball.dy *= -1
            print(ball.dy)



wn.mainloop()
