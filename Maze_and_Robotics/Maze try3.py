import numpy

# to convert from dgree to rad (x/180)*pi

# O1 and O2 are the variables of the 2 DoF system

ara = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]
side_walls = [[1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1]]
front_walls = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
direct = 0
loca = [0, 0]
des = [4, 2]
print(numpy.matrix(ara))
print(numpy.matrix(side_walls))
print(numpy.matrix(front_walls))
destination_x = 2  # int(input("Enter x access for the destination"))
destination_y = 4  # int(input("Enter y access for the destination"))
ara_weight = ara

#
# for loop1 in range(0, 5):
#     for loop2 in range(0, 5):
#         xx = loop1
#         yy = loop2


# if (destination_x + xx < len(ara_weight) - 1):
#      ara_weight[destination_x + xx][destination_y] = xx
# if (destination_x - xx < len(ara_weight) - 1):
#     ara_weight[destination_x-xx][destination_y] = xx
# if (destination_y + yy < len(ara_weight) - 1):
#     ara_weight[destination_x][destination_y+yy] = xx
# if (destination_y - yy < len(ara_weight) - 1):
#     ara_weight[destination_x][destination_y-yy] = xx


ara_weight[destination_x][destination_y] = 0

try:
    ara_weight[destination_x + 1][destination_y] = 1
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y] = 1
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 1] = 1
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 1] = 1
except IndexError:
    er = 'null'

try:
    ara_weight[destination_x + 1][destination_y + 1] = 2
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y + 1] = 2
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y - 1] = 2
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y - 1] = 2
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y] = 2
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y] = 2
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 2] = 2
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 2] = 2
except IndexError:
    er = 'null'

try:
    ara_weight[destination_x + 2][destination_y + 1] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y + 1] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y - 1] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y - 1] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y + 2] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y + 2] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y - 2] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y - 2] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 3] = 3
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 3] = 3
except IndexError:
    er = 'null'

try:
    ara_weight[destination_x + 3][destination_y + 1] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y + 1] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y - 1] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y - 1] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y + 3] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y + 3] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y - 3] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y - 3] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y + 2] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y + 2] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y - 2] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y - 2] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 4] = 4
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 4] = 4
except IndexError:
    er = 'null'

try:
    ara_weight[destination_x + 4][destination_y + 1] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y + 1] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y - 1] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y - 1] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y + 4] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y + 4] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y - 4] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y - 4] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y + 2] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y + 2] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y - 2] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y - 2] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y + 3] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y + 3] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y - 3] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y - 3] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 5][destination_y] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 5][destination_y] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 5] = 5
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 5] = 5
except IndexError:
    er = 'null'

try:
    ara_weight[destination_x + 5][destination_y + 1] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 5][destination_y + 1] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 5][destination_y - 1] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 5][destination_y - 1] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y + 5] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y + 5] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y - 5] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y - 5] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y + 3] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y + 3] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y - 3] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y - 3] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y + 4] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y + 4] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y - 4] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y - 4] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y + 2] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y + 2] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y - 2] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y - 2] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 6][destination_y] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 6][destination_y] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 6] = 6
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 6] = 6
except IndexError:
    er = 'null'

try:
    ara_weight[destination_x + 6][destination_y + 1] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 6][destination_y + 1] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 6][destination_y - 1] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 6][destination_y - 1] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y + 6] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y + 6] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y - 6] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y - 6] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y + 5] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y + 5] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y - 5] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y - 5] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 5][destination_y + 2] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 5][destination_y + 2] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 5][destination_y - 2] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 5][destination_y - 2] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y + 3] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y + 3] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y - 3] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y - 3] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y + 4] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y + 4] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y - 4] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y - 4] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 7][destination_y] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 7][destination_y] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 7] = 7
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 7] = 7
except IndexError:
    er = 'null'

try:
    ara_weight[destination_x + 7][destination_y + 1] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 7][destination_y + 1] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 7][destination_y - 1] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 7][destination_y - 1] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y + 7] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y + 7] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 1][destination_y - 7] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 1][destination_y - 7] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y + 5] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y + 5] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 3][destination_y - 5] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 3][destination_y - 5] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 5][destination_y + 3] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 5][destination_y + 3] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 5][destination_y - 3] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 5][destination_y - 3] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y + 4] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y + 4] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 4][destination_y - 4] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 4][destination_y - 4] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y + 6] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y + 6] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 2][destination_y - 6] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 2][destination_y - 6] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 6][destination_y + 2] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 6][destination_y + 2] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 6][destination_y - 2] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 6][destination_y - 2] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x + 8][destination_y] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x - 8][destination_y] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y + 8] = 8
except IndexError:
    er = 'null'
try:
    ara_weight[destination_x][destination_y - 8] = 8
except IndexError:
    er = 'null'


def loc():
    global loca
    print(loca)


def move_for(x, d):  # x number of blocks   d direction
    ##the hardawre code here
    print("moved ", x, " blocks to the front")
    if d == 0:  # direction 0 up 1 down 2 right 3 left
        loca[1] = loca[1] + x
    if d == 1:
        loca[1] = loca[1] - x
    if d == 2:
        loca[0] = loca[0] + x
    if d == 3:
        loca[0] = loca[0] - x


def move_back(x, d):
    # the hardware code here

    # write the code of the move to the back function where x is the number of blocks
    # and d is the direction of the car 0 front , 1 back , 2 right , 3 left
    pass


def rotate_left():
    global direct
    # the hardware code
    direct = 3


def rotate_right():
    global direct
    # the hardware code
    direct = 2


def rotate_front():
    global direct
    # the hardware code
    direct = 0


def rotate_back():
    global direct
    # the hardware code
    direct = 1


def see(sensor):
    pass
    # hardware code here
    # if find some thing return true else return false
    # three sensors one on the front and the second to he right and the third to the left


###################################
# def your_algorithm
########################################


print(loca)
print(direct)
move_for(2, direct)
rotate_right()

print(loca)

print(direct)
i = 0
# for row in ara_weight:
print("ara_weight: ", numpy.matrix(ara_weight))
#    i+=1

print(numpy.identity('5'[str, '0']))
