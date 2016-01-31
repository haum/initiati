#!/usr/bin/env python3

import math

class Door:
    _id = 0 # Should be static

    def __init__(self, idAngle, idRadius):
        Door._id = Door._id + 1
        self._id = Door._id 
        self._originX = 100
        self._originY = 200
        self._tagId = "square"
        self._idAngle = idAngle
        self._idRadius = idRadius
        
    def getTranslation(self):
        if (self._idRadius%2 == 0):
            offset = -22.5
        else:
            offset = 0

        angle = 90+offset-self._idAngle*45
        ratio = self._idRadius/10*177.165
        x = math.cos(math.radians(angle))*ratio
        y = math.sin(math.radians(angle))*ratio

        return (x, y)

    def getSvgPart(self):
        translateX, translateY = self.getTranslation()
        return("\
    <use\n\
       x=\"" + str(self._originX) + "\"\n\
       y=\"" + str(self._originY) + "\"\n\
       xlink:href=\"#" + self._tagId + "\"\n\
       id=\"door" + str(self._id) + "\"\n\
       transform=\"translate(" + str(translateX) + "," + str(translateY) + ")\"\n\
       width=\"744.09448\"\n\
       height=\"1052.3622\" />\
")

for i in range (0,8):
    for beta in range (9,1,-1):
        d = Door(i, beta)
        print(d.getSvgPart())
