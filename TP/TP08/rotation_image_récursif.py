from PIL import Image

mario = Image.open("mario.png")


def echange_pix(image, x0, y0, x1, y1):
    px1 = image.getpixel((x1, y1))
    image.putpixel((x1, y1), image.getpixel((x0, y0)))
    image.putpixel((x0, y0), px1)


def echange_quadrant(image, x0, y0, x1, y1, n, fois=1):
    for _ in range(fois):
        for i in range(n):
            for j in range(n):
                echange_pix(image, x0+i, y0+j, x1+i, y1+j)


def tourne_quadrant(image, x0, y0, n):
    if n>=2:
        m=n//2
        
        
        
        
echange_quadrant(mario, 0, 0, 64, 0, 64)
echange_quadrant(mario, 64, 64, 0, 0, 64)
echange_quadrant(mario, 0, 64, 0, 0, 64)

mario.show()
