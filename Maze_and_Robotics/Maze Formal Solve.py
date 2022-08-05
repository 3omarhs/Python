import numpy

ara = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
w_side = [[1, 1, 1, 0, 1], [1, 0, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 0, 1]]
w_over = [[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
data = []
locx = []
locy = []

sizex = len(ara)
sizey = len(ara[0])

loc = [0, 0]
dis = [0, 2]

data.append(1)
locx.append(dis[0])
locy.append(dis[1])

def check():
    while len(data) > 0:
        d = data.pop()
        x = locx.pop()
        y = locy.pop()
        if ((x + 1) < sizex) and checkwall(1, x, y) == 0 and (ara[x + 1][y] == 0 or (d + 1) <= ara[x + 1][y]):
            ara[x + 1][y] = d + 1
            data.append(ara[x + 1][y])
            locx.append(x + 1)
            locy.append(y)

        if ((x - 1) >= 0) and checkwall(2, x, y) == 0 and (ara[x - 1][y] == 0 or (d + 1) <= ara[x - 1][y]):
            ara[x - 1][y] = d + 1
            data.append(ara[x - 1][y])
            locx.append(x - 1)
            locy.append(y)

        if ((y + 1) < sizey) and checkwall(3, x, y) == 0 and (ara[x][y + 1] == 0 or (d + 1) <= ara[x][y + 1]):
            ara[x][y + 1] = d + 1
            data.append(ara[x][y + 1])
            locx.append(x)
            locy.append(y + 1)

        if ((y - 1) >= 0) and checkwall(4, x, y) == 0 and (ara[x][y - 1] == 0 or (d + 1) <= ara[x][y - 1]):
            ara[x][y - 1] = d + 1
            data.append(ara[x][y - 1])
            locx.append(x)
            locy.append(y - 1)

def checkwall(l, x, y):
    if l == 1:
        return w_over[x + 1][y]
    if l == 2:
        return w_over[x][y]
    if l == 3:
        return w_side[x][y + 1]
    if l == 4:
        return w_side[x][y]


check()
print(numpy.matrix(ara))
