#Ja Yoon Lee
#B06
#903008438
#jlee3018@gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials.

from Graphics import *

win = Window("Face", 600, 600)



hair = Rectangle((110, 210), (490, 600))
hair.gradient = Gradient("linear", (0, 0), Color("brown"), (0, 200), Color("black"))
hair.outline = Color("brown")
hair.draw(win)

head = Oval((300, 280), 180, 230)
head.fill = Color("lightyellow")
head.draw(win)

hair2 = Pie((300, 210), 190, 180, 360)
hair2.fill = Color("brown")
hair2.outline = Color("brown")
hair2.draw(win)

hair3 = Rectangle((110, 210), (160, 600))
hair3.gradient = Gradient("linear", (0, 0), Color("brown"), (0, 300), Color("black"))
hair3.outline = Color("brown")
hair3.draw(win)

hair4 = Rectangle((440, 210), (490, 600))
hair4.gradient = Gradient("linear", (0, 0), Color("brown"), (0, 300), Color("black"))
hair4.outline = Color("brown")
hair4.draw(win)

eyeL = Oval((230, 250), 40, 20 )
eyeL.fill = Color("white")
eyeL.border = 2
eyeL.draw(win)

eyeL2 = Circle((230, 250), 20)
eyeL2.gradient = Gradient("radial", (0, 0), 10, Color("green"), (10,10), 30, Color("lightgreen"))
eyeL2.border = 2
eyeL2.draw(win)

eyeR = Oval((370, 250), 40, 20 )
eyeR.fill = Color("white")
eyeR.border = 2
eyeR.draw(win)

eyeR2 = Circle((370, 250), 20 )
eyeR2.gradient = Gradient("radial", (0, 0), 10, Color("green"), (10,10), 30, Color("lightgreen"))
eyeR2.border = 2
eyeR2.draw(win)

eyebrowL = Curve((180, 200), (220, 190), (240, 190), (270, 200))
eyebrowL.border = 3
eyebrowL.draw(win)

eyebrowR = Curve((330, 200), (360, 190), (380, 190), (420, 200))
eyebrowR.border = 3
eyebrowR.draw(win)

nose1 = Polygon((300, 350), (300, 270), (315, 350))
nose1.fill = Color("black")
nose1.draw(win)

nose2 = Polygon((280, 350), (315, 350), (300, 360))
nose2.fill = Color("black")
nose2.draw(win)

mouth = Pie((300, 400), 50, 0, 360-180)
mouth.fill = Color("yellow")
mouth.draw(win)

tattoo1 = Polygon((200, 310), (165, 370), (235, 370))
tattoo1.fill = Color("white")
tattoo1.draw(win)

tattoo2 = Circle((200, 350), 20)
tattoo2.fill = Color("lightblue")
tattoo2.draw(win)

tattoo3 = Line((200, 310), (200, 370))
tattoo3.color = Color("blue")
tattoo3.border = 3
tattoo3.draw(win)