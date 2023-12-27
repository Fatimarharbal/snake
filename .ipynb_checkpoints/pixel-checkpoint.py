import pyxel
def update():
    pass
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
