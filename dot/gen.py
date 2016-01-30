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
	[CN, CN, CN, CN, CN, CN, CN, CN], # E left and right
	[CN, CN, CN, CN, CN, CN, CN, CN], # E bottom
	[CN, CN, CN, CN, CN, CN, CN, CN], # D left and right
	[CN, CN, CN, CN, CN, CN, CN, CN], # D bottom
	[CN, CN, CN, CN, CN, CN, CN, CN], # C left and right
	[CN, CN, CN, CN, CN, CN, CN, CN], # C bottom
	[CN, CN, CN, CN, CN, CN, CN, CN], # B left and right
	[CB, CN, CN, CN, CN, CN, CN, CN], # B bottom
]

print('digraph G {')

for x in range(7):
	for y in range(8):
		door = DOORS[x][y]
		if door != CN:
			if x % 2:
				print('\t' + precedent(door) + ring(x) + case1(y) + " -> " + door + ring(x+2) + case1(y) + " // BOTTOM " + str(x) + " " + str(y) + " " + door)
				print('\t' + precedent(door) + ring(x+2) + case1(y) + " -> " + door + ring(x) + case1(y) + " // BOTTOM " + str(x) + " " + str(y) + " " + door)
			else:
				print('\t' + precedent(door) + ring(x) + case1(y) + " -> " + door + ring(x) + case1(y - 1) + " // LR " + str(x) + " " + str(y) + " " + door)
				print('\t' + precedent(door) + ring(x) + case1(y - 1) + " -> " + door + ring(x) + case1(y) + " // LR " + str(x) + " " + str(y) + " " + door)

for y in range(8):
	door = DOORS[7][y]
	if door != CN:
		print('\t' + precedent(door) + ring(6) + case1(y) + " -> " + door + "A0" + " // BOTTOM_B " + str(y) + " " + door)
		print('\t' + precedent(door) + "A0 -> " + door + ring(6) + case1(y) + " // BOTTOM_B " + str(y) + " " + door)
	
for y in range(8):
	door = DOORS[7][y]
	if door != CN:
		print("\tA0 -> " + door + ring(6) + case1(y) + " // BOTTOM_A0 " + str(y) + " " + door)

print('}')
