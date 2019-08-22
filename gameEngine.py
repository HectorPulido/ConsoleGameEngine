import math


class gameEngine:
    def __init__(self, room, screenSize, pov, minStep, minStepAngle, maxDistance, wallHeight):
        self.roomMatrix = room.split("\n")
        self.screenSize = screenSize
        self.pov = pov
        self.minStep = minStep
        self.minStepAngle = minStepAngle
        self.maxDistance = maxDistance
        self.wallHeight = wallHeight
        self.roomSize = (len(self.roomMatrix), len(self.roomMatrix[0]))

    def drange(self, start, stop, step):
        r = start
        while r < stop:
            yield r
            r += step

    def calcDistance(self, position, angle):
        distance = self.minStep
        while distance <= self.maxDistance:
            distance += self.minStep
            targetPosX = (int)(math.cos(math.radians(angle))
                               * distance + position[0])
            targetPosY = (int)(math.sin(math.radians(angle))
                               * distance + position[1])

            if targetPosX < 0 or targetPosY < 0 or targetPosX >= self.screenSize[0] \
                    or targetPosY >= self.screenSize[1]:
                return -1

            if self.roomMatrix[targetPosX][targetPosY] != ".":
                return distance

        return -1

    def calcPov(self, position, angle):
        distances = []

        for i in range(self.screenSize[0]):
            rayAngle = (angle - self.pov/2) + (i/self.screenSize[0]) * self.pov
            value = self.calcDistance(position, rayAngle)
            distances.append(value)

        return distances

    def getScreen(self, position, angle):
        view = self.calcPov(position, angle)

        output = ""
        for j in range(self.screenSize[1]):
            for i in view:
                if math.fabs(self.screenSize[1]/2 - j) <= (self.wallHeight - i):
                    s = " "
                    if i == -1:
                        if (self.screenSize[1]/2 - j) < 0:
                            output += "."
                        else:
                            output += " "
                    elif i >= 0 and i < 4:
                        s = u"\u2588"
                    elif i >= 4 and i < 8:
                        s = u"\u2593"
                    elif i >= 8 and i < 12:
                        s = u"\u2592"
                    elif i >= 10 and i < 15:
                        s = u"\u2591"
                    else:
                        if (self.screenSize[1]/2 - j) < 0:
                            output += "."
                        else:
                            output += " "

                    output += s
                else:
                    if (self.screenSize[1]/2 - j) < 0:
                        output += "."
                    else:
                        output += " "
            output += "\n"

        return output
