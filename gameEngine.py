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

    def getBlock(self, distance):
        if distance >= 0 and distance < 4:
            return u"\u2588"
        elif distance >= 4 and distance < 8:
            return u"\u2593"
        elif distance >= 8 and distance < 12:
            return u"\u2592"
        elif distance >= 10 and distance < 15:
            return u"\u2591"
        return -1

    def getEmpty(self, screenPoint):
        screenPoint *= -1

        if screenPoint < 5:
            return "."
        elif screenPoint < 10 and screenPoint >= 5:
            return "-"
        elif screenPoint < 15 and screenPoint >= 10:
            return "X"
        return "#"

    def getScreen(self, position, angle):
        view = self.calcPov(position, angle)

        output = ""
        for j in range(self.screenSize[1]):
            for i in view:
                if math.fabs(self.screenSize[1]/2 - j) <= (self.wallHeight - i):
                    s = self.getBlock(i)
                    if s == -1:
                        if (self.screenSize[1]/2 - j) < 0:
                            s = self.getEmpty(self.screenSize[1]/2 - j)
                        else:
                            s = " "

                    output += s
                else:
                    if (self.screenSize[1]/2 - j) < 0:
                        output += self.getEmpty(self.screenSize[1]/2 - j)
                    else:
                        output += " "
            output += "\n"

        return output
