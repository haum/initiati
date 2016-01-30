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
	[CN, CR, CG, CB, CB, CB, CN, CR], # E left and right
	  [CB, CN, CN, CR, CG, CR, CG, CB], # E bottom
	[CG, CG, CB, CG, CR, CR, CB, CG], # D left and right
	  [CR, CR, CB, CB, CG, CG, CN, CR], # D bottom
	[CN, CB, CG, CN, CR, CB, CN, CB], # C left and right
	  [CG, CG, CR, CG, CB, CN, CG, CN], # C bottom
	[CN, CB, CN, CG, CR, CR, CG, CR], # B left and right
	  [CR, CN, CB, CB, CB, CN, CB, CB], # B bottom
]

print('digraph G {')
print('A0 [shape = doublecircle];')

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
