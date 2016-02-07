#!/usr/bin/env python3

CR = 'Circle'
CG = 'Triangle'
CB = 'Square'

DOORS = [
	[CG, CR, CG, CB, CB, CB, CB, CR], # E left and right
	  [CB, CB, CR, CR, CG, CR, CG, CB], # E bottom
	[CG, CG, CB, CG, CR, CR, CB, CG], # D left and right
	  [CR, CR, CB, CB, CG, CG, CR, CR], # D bottom
	[CG, CB, CG, CG, CR, CB, CR, CB], # C left and right
	  [CG, CG, CR, CG, CB, CG, CG, CG], # C bottom
	[CR, CB, CB, CG, CR, CR, CG, CR], # B left and right
	  [CR, CG, CB, CB, CB, CR, CB, CB], # B bottom
]

import math

class Door:
    _id = 0 # Should be static

    def factory(idAngle, idRadius):
        klass = DOORS[7-(idRadius)][idAngle]
        if(klass=='Circle'):
            return Circle(idAngle, idRadius)
        elif(klass=='Square'):
            return Square(idAngle, idRadius)
        elif(klass=='Triangle'):
            return Triangle(idAngle, idRadius)

    def __init__(self, idAngle, idRadius):
        Door._id = Door._id + 1
        self._id = Door._id 
        self._originX = 600
        self._originY = 600
        self._tagId = "dummy"
        self._idAngle = idAngle
        self._idRadius = idRadius
        
    def getTranslation(self):
        if (self._idRadius%2 == 0):
            offset_angle = -22.5
            offset = 0
        else:
            offset_angle = 0
            offset = -2.5

        angle = 90+offset_angle-self._idAngle*45
        ratio = 75 + self._idRadius * 50 + offset
        x = math.sin(math.radians(angle))*ratio
        y = math.cos(math.radians(angle))*ratio

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
       width=\"500\"\n\
       height=\"500\" />\
")

A3Hpx = 1488.18898
A3Wpx = 1052.36220
CX = 50
CY = - A3Hpx + 880

class Circle(Door):
    def __init__(self, idAngle, idRadius):
        Door.__init__(self, idAngle, idRadius)
        self._originX = A3Wpx/2 + CX
        self._originY = A3Hpx/2 + CY - 80
        self._tagId = "circle"
        
class Square(Door):
    def __init__(self, idAngle, idRadius):
        Door.__init__(self, idAngle, idRadius)
        self._originX = A3Wpx/2 + CX
        self._originY = A3Hpx/2 + CY
        self._tagId = "square"

class Triangle(Door):
    def __init__(self, idAngle, idRadius):
        Door.__init__(self, idAngle, idRadius)
        self._originX = A3Wpx/2 + CX
        self._originY = A3Hpx/2 + CY - 160
        self._tagId = "triangle"

for i in range (0,8):
    for beta in range (0,8):
        d = Door.factory(i, beta)
        print(d.getSvgPart())
