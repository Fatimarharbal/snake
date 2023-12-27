
import pyxel
import time

t1 = time.time()


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    global t1
    t2 = time.time()
    dt = t2 - t1
    t1 = t2
    fps = 1.0/dt
    fps = int(round(fps))
    pyxel.cls(7) #color le fond d'écran 
    color = pyxel.frame_count % 16 #clignotement du texte avec 16 couleurs 
    pyxel.text(56, 54, "Hello Snake!", color) #affiche le texte
    pyxel.text(0,0, f"fps: {fps}", 0)

pyxel.init(160, 120, fps = 30)
pyxel.run(update,draw)
pyxel.show()



def pixel():
    for i in range (30):
        for j in range(30):
            if (i+j) % 2 == 0:
                col = 7
            else : 
                col = 13
            pyxel.pset(i,j,col)

pyxel.init(30,30)
pyxel.run(update,pixel)






