from gameEngine import gameEngine
from osUtils import getch, clear
import math
import time

room = ""
room += "######################################################\n"
room += "######################################################\n"
room += "######################....############################\n"
room += "######################....############################\n"
room += "######################....############################\n"
room += "#############......................###################\n"
room += "#############......................###################\n"
room += "#############......................###################\n"
room += "######################....############################\n"
room += "######################....############################\n"
room += "######################....############################\n"
room += "######################################################\n"
room += "######################################################\n"

screenSize = (90, 40)
position = [7, 25]
angle = 45
pov = 100
minStep = 0.1
minStepAngle = 0.1
maxDistance = 15
wallHeight = 20

angleSpeed = 30
movementSpeed = 2


engine = gameEngine(room, screenSize, pov, minStep,
                    minStepAngle, maxDistance, wallHeight)

clear()
print(engine.getScreen(position, angle))

start = time.clock()

while True:
    end = time.clock()
    diff = end - start
    start = end

    try:
        pressedkey = getch().decode('utf-8')
    except UnicodeDecodeError:
        continue

    if pressedkey == 'w' or pressedkey == 'W':
        position[0] = position[0] + \
            math.cos(math.radians(angle)) * movementSpeed * diff
        position[1] = position[1] + \
            math.sin(math.radians(angle)) * movementSpeed * diff
    if pressedkey == 's' or pressedkey == 'S':
        position[0] = position[0] - \
            math.cos(math.radians(angle)) * movementSpeed * diff
        position[1] = position[1] - \
            math.sin(math.radians(angle)) * movementSpeed * diff
    if pressedkey == 'a' or pressedkey == 'A':
        angle -= angleSpeed * diff
    if pressedkey == 'd' or pressedkey == 'D':
        angle += angleSpeed * diff
    if pressedkey == 'e' or pressedkey == 'E':
        break

    clear()
    print(engine.getScreen(position, angle))
    print("posicion: ", position)
    print("angulo: ", angle)
    print("wallHeight: ", wallHeight)
    print("pressedkey: ", pressedkey)
    print("diff Time: ", diff)
