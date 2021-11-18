from tkinter import *
import time

root = Tk()


def balls():
    vert_vitesse_x, vert_vitesse_y = [5, 3]
    rouge_vitesse_x, rouge_vitesse_y = [5, 3]

    canvas = Canvas(root, width=800, height=800, bg="grey")
    root.title("Detection des murs")
    canvas.grid()

    balle_verte = canvas.create_oval(20, 20, 30, 10, fill="green")
    balle_rouge = canvas.create_oval(780, 780, 790, 790, fill="red")

    while True:
        canvas.move(balle_verte, vert_vitesse_x, vert_vitesse_y)
        vert_coord = canvas.coords(balle_verte)
        if vert_coord[3] >= 800 or vert_coord[1] <= 0:
            vert_vitesse_y = -vert_vitesse_y
        if vert_coord[2] >= 800 or vert_coord[0] <= 0:
            vert_vitesse_x = -vert_vitesse_x

        canvas.move(balle_rouge, rouge_vitesse_x, rouge_vitesse_y)
        rouge_coord = canvas.coords(balle_rouge)
        if rouge_coord[3] >= 800 or rouge_coord[1] <= 0:
            rouge_vitesse_y = -rouge_vitesse_y
        if rouge_coord[2] >= 800 or rouge_coord[0] <= 0:
            rouge_vitesse_x = -rouge_vitesse_x

        time.sleep(0.01)
        root.update()


balls()
root.mainloop()
