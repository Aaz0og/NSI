import tkinter as tk

root = tk.Tk()

width = 900
height = 500

canvas = tk.Canvas(root, bg='white', width=width, height=height)
canvas.pack()

ball = canvas.create_oval(430, 10, 470, 50, fill='green')

# ball moving speed
xspeed = yspeed = 2

def move_ball():
  global xspeed, yspeed
  x1, y1, x2, y2 = canvas.coords(ball)
  if x1 <= 0 or x2 >= width:
    # hit wall, reverse x speed
    xspeed = -xspeed
  if y1 <= 0:
    # hit top wall
    yspeed = 2
  elif y2 >= platform_y:
    # calculate center x of the ball
    cx = (x1 + x2) // 2
    # check whether platform is hit
    px1, _, px2, _ = canvas.coords(platform)
    if px1 <= cx <= px2:
      yspeed = -2
    else:
      canvas.create_text(width//2, height//2, text='Game Over', font=('Arial Bold', 32), fill='red')
      return
  canvas.move(ball, xspeed, yspeed)
  canvas.after(20, move_ball)

move_ball()

root.mainloop()