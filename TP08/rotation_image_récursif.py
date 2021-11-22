from PIL import Image

def echange_pix(image,x0,y0,x1,y1):
    for y_boucle in range(128):
        for x_boucle in range(128):
            

img= Image.open("mario.png")
echange_pix(img)
