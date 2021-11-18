from tkinter import *
import time

root = Tk()


def balls():
    green_x_speed, green_y_speed = [5,3]
    red_x_speed, red_y_speed = [5,3]

    canvas = Canvas(root, width=800, height=800, bg="grey")
    root.title("collision detection")
    canvas.grid()

    green_ball = canvas.create_oval(20, 20, 30, 10, fill="green")
    red_ball = canvas.create_oval(780, 780, 790, 790, fill="red")

    while True:
        canvas.move(green_ball, green_x_speed, green_y_speed)
        green_coordinates = canvas.coords(green_ball)
        if green_coordinates[3] >= 800 or green_coordinates[1] <= 0:
            green_y_speed = -green_y_speed
        if green_coordinates[2] >= 800 or green_coordinates[0] <= 0:
            green_x_speed = -green_x_speed

        canvas.move(red_ball, red_x_speed, red_y_speed)
        red_coordinates = canvas.coords(red_ball)
        if red_coordinates[3] >= 800 or red_coordinates[1] <= 0:
            red_y_speed = -red_y_speed
        if red_coordinates[2] >= 800 or red_coordinates[0] <= 0:
            red_x_speed = -red_x_speed

        time.sleep(0.01)
        root.update()

balls()
root.mainloop()