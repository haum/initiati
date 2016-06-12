CG="CG"
CR="CR"
CB="CB"

DOORS = [
	  [CB, CR, CR, CB, CG, CB, CR, CG], # outter ring
	[CG, CR, CG, CB, CB, CB, CB, CR],   # E left and right
	  [CB, CB, CR, CR, CG, CR, CG, CB], # E bottom
	[CG, CG, CB, CG, CR, CR, CB, CG],   # D left and right
	  [CR, CR, CB, CB, CG, CG, CR, CR], # D bottom
	[CG, CB, CG, CG, CR, CB, CR, CB],   # C left and right
	  [CG, CG, CR, CG, CB, CG, CG, CG], # C bottom
	[CR, CB, CB, CG, CR, CR, CG, CR],   # B left and right
	  [CR, CG, CB, CB, CB, CR, CB, CB], # B bottom
]


HEADER = """\\documentclass[a3paper]{article}
\\usepackage{tikz}
\\newcommand\CG[2]{\\fill[green] (-#2:#1) circle (.1);}
\\newcommand\CR[2]{\\fill[red] (-#2:#1) circle (.1);}
\\newcommand\CB[2]{\\fill[blue] (-#2:#1) circle (.1);}
\\usepackage[top=0.5cm,bottom=0.5cm,left=0.5cm,right=0.5cm]{geometry}
\\begin{document}
\\begin{figure}
\\centering
\\begin{tikzpicture}[scale=1.5]
"""

FOOTER = """\\end{tikzpicture}
\\end{figure}
\\end{document}
"""

print(HEADER)


for i in range(len(DOORS[0])):
    print('\\draw[very thick, black!50] ('+str(-i*360/len(DOORS[0]))+':1) -- ++('+str(-i*360/len(DOORS[0]))+':'+str(len(DOORS)&~1)+');')

radius = 0
angle_step = 45
for n,ring in enumerate(reversed(DOORS)):
    radius += 1
    if n%2==0: # bottom ring
        angle_shift = 22.5
        print('\\draw[black!50, very thick] (0,0) circle ('+str(radius)+');')
    else:
        angle_shift = 0
    for i,dottype in enumerate(ring):
        print("\\"+dottype+"{"+str(radius)+"}{"+str(angle_shift+angle_step*i)+"};")

if len(DOORS)%2 == 0:
    print('\\draw[black!50, very thick] (0,0) circle ('+str(len(DOORS)+1)+');')

print(FOOTER)
