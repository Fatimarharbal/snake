import pyxel 
import time 
import random
snake_geometry = [[10,15],[11,15],[12,15]]
keys = [pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_RIGHT, pyxel.KEY_LEFT]
snake_direction =[1,0]
def update():
    global snake_direction, snake_geometry
    keys_pressed = []
    for key in keys:
        if pyxel.btnp(key):
            keys_pressed.append(key)
    for key in keys_pressed:
        if key == pyxel.KEY_UP:
            snake_direction = [0,-1]
        elif key == pyxel.KEY_DOWN:
            snake_direction = [0,1]
        elif key == pyxel.KEY_RIGHT:
            snake_direction = [1,0]
        elif key == pyxel.KEY_LEFT:
            snake_direction = [-1,0]
    

def draw():
    for i in range (30):
        for j in range(30):
            if (i+j) % 2 == 0:
                col = 7
            else : 
                col = 13
            pyxel.pset(i,j,col)
    pyxel.pset(random.randint(0,30),random.randint(0,30),8)
    pyxel.pset(snake_geometry[0][0],snake_geometry[0][1], 3)
    pyxel.pset(snake_geometry[1][0],snake_geometry[1][1], 3)
    pyxel.pset(snake_geometry[2][0],snake_geometry[2][1], 11)
pyxel.init(30,30)
pyxel.run(update,draw)
