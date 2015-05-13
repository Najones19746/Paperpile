__author__ = 'Nick Jones'
f = open("rects.in")
raw = f.readline()
width, height = raw.split()
width = int(width)
height = int(height)
paper = []
colorcount = {}
for x in range(0, width ):
    line = []
    for y in range(0, height):
        line.append('0')
    paper.append(line)


for lines in f:
    color, sx, sy, sw, sh = lines.split()
    sx = int(sx)
    sy = int(sy)
    sw = int(sw)
    sh = int(sh)
    for x in range(sx, sx + sw):
        for y in range(sy, sy + sh):
            paper[x][y] = color

for x in range(0, width):
    for y in range(0, height):

        if str(paper[x][y]) in colorcount:
            colorcount[paper[x][y]] += 1
        else:
            colorcount[paper[x][y]] = 1

for key in colorcount.keys():
    print "color: %s count: %s" % (key, str(colorcount[key]))