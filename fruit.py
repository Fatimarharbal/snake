import pyxel
import time
import random

obstacle = []
for i in range(30):
    for j in range(30):
        if (i + j) % 5 == 0 and (i - j) % 10 == 0:
            obstacle.append([i, j])

fruit = [random.randint(0, 30), random.randint(0, 30)]
snake_geometry = [[10, 15], [11, 15], [12, 15]]
keys = [pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_RIGHT, pyxel.KEY_LEFT]
snake_direction = [1, 0]


def update():
    global snake_direction, snake_geometry, fruit
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    keys_pressed = []
    for key in keys:
        if pyxel.btnp(key):
            keys_pressed.append(key)
    for key in keys_pressed:
        if key == pyxel.KEY_UP:
            snake_direction = [0, -1]
        elif key == pyxel.KEY_DOWN:
            snake_direction = [0, 1]
        elif key == pyxel.KEY_RIGHT:
            snake_direction = [1, 0]
        elif key == pyxel.KEY_LEFT:
            snake_direction = [-1, 0]
    snake_head = snake_geometry[-1]
    new_head = [snake_head[0] + snake_direction[0], snake_head[1] + snake_direction[1]]
    snake_geometry = snake_geometry[1:] + [new_head]
    if (new_head[0] == fruit[0] and new_head[1] == fruit[1]) or (
        new_head[0] > fruit[0] - 1
        and new_head[0] < fruit[0] + 1
        and new_head[1] > fruit[1] - 1
        and new_head[1] < fruit[1] + 1
    ):
        fruit = [random.randint(0, 30), random.randint(0, 30)]
        snake_geometry = snake_geometry + [new_head]
    if new_head[0] > 30 or new_head[1] > 30 or new_head[0] < 0 or new_head[1] < 0:
        snake_geometry = [[10, 15], [11, 15], [12, 15]]
    if new_head in obstacle:
        snake_geometry = [[10, 15], [11, 15], [12, 15]]
    if fruit in obstacle:
        fruit = [random.randint(0, 30), random.randint(0, 30)]
    


def draw():
    pyxel.cls(7)
    for k in range(len(obstacle)):
        pyxel.pset(obstacle[k][0], obstacle[k][1], 0)
    pyxel.pset(fruit[0], fruit[1], 8)
    for x, y in snake_geometry[:-1]:
        pyxel.pset(x, y, 3)
    snake_head = snake_geometry[-1]
    pyxel.pset(snake_head[0], snake_head[1], 11)


pyxel.init(30, 30, fps=5)
pyxel.run(update, draw)
