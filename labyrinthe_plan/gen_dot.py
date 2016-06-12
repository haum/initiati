from itertools import product

CN = 'N'
CR = 'R'
CG = 'V'
CB = 'B'

def precedent(color):
	if color == CN:
		return CN
	if color == CR:
		return CB
	if color == CB:
		return CG
	if color == CG:
		return CR

def colorname(color):
	if color == CN:
		return 'black'
	if color == CR:
		return 'red'
	if color == CB:
		return 'blue'
	if color == CG:
		return 'green'

def case1(y):
	y += 1
	if y <= 0:
		y += 8
	if y > 8:
		y -= 8
	return str(y)

def ring(x):
	x /= 2
	x = int(x)
	if x < 0 or x >= 5:
		return 'ERROR'
	return ['E', 'D', 'C', 'B', 'A'][x]

DOORS = [
	[CG, CR, CG, CB, CB, CB, CB, CR], # E left and right
	  [CB, CB, CR, CR, CG, CR, CG, CB], # E bottom
	[CG, CG, CB, CG, CR, CR, CB, CG], # D left and right
	  [CR, CR, CB, CB, CG, CG, CR, CR], # D bottom
	[CG, CB, CG, CG, CR, CB, CR, CB], # C left and right
	  [CG, CG, CR, CG, CB, CG, CG, CG], # C bottom
	[CR, CB, CB, CG, CR, CR, CG, CR], # B left and right
	  [CR, CG, CB, CB, CB, CG, CB, CB], # B bottom
]

print('digraph G {')
print('RA0 [shape = doublecircle,color=red];')
print('VA0 [shape = doublecircle,color=green];')
print('BA0 [shape = doublecircle,color=blue];')

for x in range(7):
	for y in range(8):
		door = DOORS[x][y]
		if door != CN:
			if x % 2:
				print('\t' + precedent(door) + ring(x) + case1(y) + " -> " + door + ring(x+2) + case1(y) + "[color=" + colorname(door) + "] // BOTTOM " + str(x) + " " + str(y) + " " + door)
				print('\t' + precedent(door) + ring(x+2) + case1(y) + " -> " + door + ring(x) + case1(y) + "[color=" + colorname(door) + "] // BOTTOM " + str(x) + " " + str(y) + " " + door)
			else:
				print('\t' + precedent(door) + ring(x) + case1(y) + " -> " + door + ring(x) + case1(y - 1) + "[color=" + colorname(door) + "] // LR " + str(x) + " " + str(y) + " " + door)
				print('\t' + precedent(door) + ring(x) + case1(y - 1) + " -> " + door + ring(x) + case1(y) + "[color=" + colorname(door) + "] // LR " + str(x) + " " + str(y) + " " + door)

for y in range(8):
	door = DOORS[7][y]
	if door != CN:
		print('\t' + precedent(door) + ring(6) + case1(y) + " -> " + door + "A0 [color=" + colorname(door) + "] // BOTTOM_B " + str(y) + " " + door)
		print('\t' + precedent(door) + "A0 -> " + door + ring(6) + case1(y) + " [color=" + colorname(door) + "] // BOTTOM_B " + str(y) + " " + door)

for i in product("BCDE", "12345678"):
	print('R' + "".join(i) + " [color=red];")
	print('V' + "".join(i) + " [color=green];")
	print('B' + "".join(i) + " [color=blue];")

print('}')
