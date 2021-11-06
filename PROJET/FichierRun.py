    ball.dy-=g
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        # mur droite
        if ball.xcor()>300:
            ball.dx *=-1
        #mur gauche
        if ball.xcor()< -300:
            ball.dx*=-1
        # Regarde si doit rebondir sur sol
        if ball.ycor()< -300:
    