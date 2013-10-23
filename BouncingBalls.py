from Graphics import *
from Myro import timer
from random import random

WINSIZE = 500
NUMBALLS = 75

win = Window("PONG", WINSIZE, WINSIZE)
win.mode = "manual"

balls = []
dx = []
dy = []


def handleKeyPress(win, event):
    print("HKP was called!")
    print(event.key)
    for idx in range (len(dy)):
        dy[idx] = -dy[idx]
        dx[idx] = -dx[idx]
        #interactive with user

onKeyPress (handleKeyPress)

for x in range(NUMBALLS):
    startX = random() * WINSIZE
    startY = random() * WINSIZE
    randRadius = random()*25 -2

    ball = Circle( (startX, startY), randRadius)

    randR = random()*255
    randG = random()*255
    randB = random()*255

    ball.color = Color(randR, randG, randB)
    ball.draw(win)
    balls.append(ball)

    rdx = (random() * 40) - 20
    rdy = (random() * 40) - 20
    dx.append(rdx)
    dy.append(rdy)


#random.random()

for i in timer(15):

    for i in range(len(balls)):
        b = balls[i]
        b.move(dx[i], dy[i])
        if b.getY() > WINSIZE or b.getY() < 0:
            dy[i] = -dy[i]
        if b.getX() > WINSIZE or b.getX() < 0:
            dx[i] = -dx[i]

    win.update()
    wait(0.1)