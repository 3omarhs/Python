import numpy

# to convert from dgree to rad (x/180)*pi

# O1 and O2 are the variables of the 2 DoF system

ara = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];
side_walls = [[1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1]];
front_walls = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]];
inside_walls = [[0, 1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0]]
direct = 0;
loca = [0, 0];
des = [2, 2];
print(numpy.matrix(ara))
print(numpy.matrix(side_walls))
print(numpy.matrix(front_walls))
destination_x = des[0] #int(input("Enter x access for the destination"))
destination_y = des[1] #int(input("Enter y access for the destination"))
ara_weight =  [[9,9,9,9,9],
           [9,9,9,9,9],
           [9,9,9,9,9],
           [9,9,9,9,9],
           [9,9,9,9,9]]

sum_ara = [[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]
walls_array = sum_ara
# zipped_lists = (side_walls, front_walls)
# sum_ara = [x + y for (x, y) in zipped_lists]

new_column = [1, 0, 0, 0, 0, 1]
front = numpy.insert(front_walls, 1, new_column, axis=1)

new_row = [1, 0, 0, 0, 0, 1]
side = numpy.insert(side_walls, 1, new_row, axis=0)


for row in range(len(sum_ara)):
    for column in range(len(sum_ara)):
        if side[row][column] == 0 or front[row][column] == 0:
            sum_ara[row][column] = side[row][column] + front[row][column]
        else:
            sum_ara[row][column] = 1

for row in range(len(sum_ara)):
    for column in range(len(sum_ara)):
        if inside_walls[row][column] == 0 or sum_ara[row][column] == 0:
            walls_array[row][column] = inside_walls[row][column] + sum_ara[row][column]
        else:
            walls_array[row][column] = 1

for loop1 in range(0, 5):
    for loop2 in range(0, 5):
        xx = loop1
        yy = loop2



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
    ara_weight[destination_x - 1][destination_y] = 1
    ara_weight[destination_x][destination_y + 1] = 1
    ara_weight[destination_x][destination_y - 1] = 1

    ara_weight[destination_x + 1][destination_y + 1] = 2
    ara_weight[destination_x - 1][destination_y + 1] = 2
    ara_weight[destination_x + 1][destination_y - 1] = 2
    ara_weight[destination_x - 1][destination_y - 1] = 2
    ara_weight[destination_x + 2][destination_y] = 2
    ara_weight[destination_x - 2][destination_y] = 2
    ara_weight[destination_x][destination_y + 2] = 2
    ara_weight[destination_x][destination_y - 2] = 2

    ara_weight[destination_x + 2][destination_y + 1] = 3
    ara_weight[destination_x - 2][destination_y + 1] = 3
    ara_weight[destination_x + 2][destination_y - 1] = 3
    ara_weight[destination_x - 2][destination_y - 1] = 3
    ara_weight[destination_x + 1][destination_y + 2] = 3
    ara_weight[destination_x - 1][destination_y + 2] = 3
    ara_weight[destination_x + 1][destination_y - 2] = 3
    ara_weight[destination_x - 1][destination_y - 2] = 3
    ara_weight[destination_x + 3][destination_y] = 3
    ara_weight[destination_x - 3][destination_y] = 3
    ara_weight[destination_x][destination_y + 3] = 3
    ara_weight[destination_x][destination_y - 3] = 3

    ara_weight[destination_x + 3][destination_y + 1] = 4
    ara_weight[destination_x - 3][destination_y + 1] = 4
    ara_weight[destination_x + 3][destination_y - 1] = 4
    ara_weight[destination_x - 3][destination_y - 1] = 4
    ara_weight[destination_x + 1][destination_y + 3] = 4
    ara_weight[destination_x - 1][destination_y + 3] = 4
    ara_weight[destination_x + 1][destination_y - 3] = 4
    ara_weight[destination_x - 1][destination_y - 3] = 4
    ara_weight[destination_x + 2][destination_y + 2] = 4
    ara_weight[destination_x - 2][destination_y + 2] = 4
    ara_weight[destination_x + 2][destination_y - 2] = 4
    ara_weight[destination_x - 2][destination_y - 2] = 4
    ara_weight[destination_x + 4][destination_y] = 4
    ara_weight[destination_x - 4][destination_y] = 4
    ara_weight[destination_x][destination_y + 4] = 4
    ara_weight[destination_x][destination_y - 4] = 4

    ara_weight[destination_x + 4][destination_y + 1] = 5
    ara_weight[destination_x - 4][destination_y + 1] = 5
    ara_weight[destination_x + 4][destination_y - 1] = 5
    ara_weight[destination_x - 4][destination_y - 1] = 5
    ara_weight[destination_x + 1][destination_y + 4] = 5
    ara_weight[destination_x - 1][destination_y + 4] = 5
    ara_weight[destination_x + 1][destination_y - 4] = 5
    ara_weight[destination_x - 1][destination_y - 4] = 5
    ara_weight[destination_x + 3][destination_y + 2] = 5
    ara_weight[destination_x - 3][destination_y + 2] = 5
    ara_weight[destination_x + 3][destination_y - 2] = 5
    ara_weight[destination_x - 3][destination_y - 2] = 5
    ara_weight[destination_x + 2][destination_y + 3] = 5
    ara_weight[destination_x - 2][destination_y + 3] = 5
    ara_weight[destination_x + 2][destination_y - 3] = 5
    ara_weight[destination_x - 2][destination_y - 3] = 5
    ara_weight[destination_x + 5][destination_y] = 5
    ara_weight[destination_x - 5][destination_y] = 5
    ara_weight[destination_x][destination_y + 5] = 5
    ara_weight[destination_x][destination_y - 5] = 5

    ara_weight[destination_x + 5][destination_y + 1] = 6
    ara_weight[destination_x - 5][destination_y + 1] = 6
    ara_weight[destination_x + 5][destination_y - 1] = 6
    ara_weight[destination_x - 5][destination_y - 1] = 6
    ara_weight[destination_x + 1][destination_y + 5] = 6
    ara_weight[destination_x - 1][destination_y + 5] = 6
    ara_weight[destination_x + 1][destination_y - 5] = 6
    ara_weight[destination_x - 1][destination_y - 5] = 6
    ara_weight[destination_x + 3][destination_y + 3] = 6
    ara_weight[destination_x - 3][destination_y + 3] = 6
    ara_weight[destination_x + 3][destination_y - 3] = 6
    ara_weight[destination_x - 3][destination_y - 3] = 6
    ara_weight[destination_x + 2][destination_y + 4] = 6
    ara_weight[destination_x - 2][destination_y + 4] = 6
    ara_weight[destination_x + 2][destination_y - 4] = 6
    ara_weight[destination_x - 2][destination_y - 4] = 6
    ara_weight[destination_x + 4][destination_y + 2] = 6
    ara_weight[destination_x - 4][destination_y + 2] = 6
    ara_weight[destination_x + 4][destination_y - 2] = 6
    ara_weight[destination_x - 4][destination_y - 2] = 6
    ara_weight[destination_x + 6][destination_y] = 6
    ara_weight[destination_x - 6][destination_y] = 6
    ara_weight[destination_x][destination_y + 6] = 6
    ara_weight[destination_x][destination_y - 6] = 6

    ara_weight[destination_x + 6][destination_y + 1] = 7
    ara_weight[destination_x - 6][destination_y + 1] = 7
    ara_weight[destination_x + 6][destination_y - 1] = 7
    ara_weight[destination_x - 6][destination_y - 1] = 7
    ara_weight[destination_x + 1][destination_y + 6] = 7
    ara_weight[destination_x - 1][destination_y + 6] = 7
    ara_weight[destination_x + 1][destination_y - 6] = 7
    ara_weight[destination_x - 1][destination_y - 6] = 7
    ara_weight[destination_x + 2][destination_y + 5] = 7
    ara_weight[destination_x - 2][destination_y + 5] = 7
    ara_weight[destination_x + 2][destination_y - 5] = 7
    ara_weight[destination_x - 2][destination_y - 5] = 7
    ara_weight[destination_x + 5][destination_y + 2] = 7
    ara_weight[destination_x - 5][destination_y + 2] = 7
    ara_weight[destination_x + 5][destination_y - 2] = 7
    ara_weight[destination_x - 5][destination_y - 2] = 7
    ara_weight[destination_x + 4][destination_y + 3] = 7
    ara_weight[destination_x - 4][destination_y + 3] = 7
    ara_weight[destination_x + 4][destination_y - 3] = 7
    ara_weight[destination_x - 4][destination_y - 3] = 7
    ara_weight[destination_x + 3][destination_y + 4] = 7
    ara_weight[destination_x - 3][destination_y + 4] = 7
    ara_weight[destination_x + 3][destination_y - 4] = 7
    ara_weight[destination_x - 3][destination_y - 4] = 7
    ara_weight[destination_x + 7][destination_y] = 7
    ara_weight[destination_x - 7][destination_y] = 7
    ara_weight[destination_x][destination_y + 7] = 7
    ara_weight[destination_x][destination_y - 7] = 7

    ara_weight[destination_x + 7][destination_y + 1] = 8
    ara_weight[destination_x - 7][destination_y + 1] = 8
    ara_weight[destination_x + 7][destination_y - 1] = 8
    ara_weight[destination_x - 7][destination_y - 1] = 8
    ara_weight[destination_x + 1][destination_y + 7] = 8
    ara_weight[destination_x - 1][destination_y + 7] = 8
    ara_weight[destination_x + 1][destination_y - 7] = 8
    ara_weight[destination_x - 1][destination_y - 7] = 8
    ara_weight[destination_x + 3][destination_y + 5] = 8
    ara_weight[destination_x - 3][destination_y + 5] = 8
    ara_weight[destination_x + 3][destination_y - 5] = 8
    ara_weight[destination_x - 3][destination_y - 5] = 8
    ara_weight[destination_x + 5][destination_y + 3] = 8
    ara_weight[destination_x - 5][destination_y + 3] = 8
    ara_weight[destination_x + 5][destination_y - 3] = 8
    ara_weight[destination_x - 5][destination_y - 3] = 8
    ara_weight[destination_x + 4][destination_y + 4] = 8
    ara_weight[destination_x - 4][destination_y + 4] = 8
    ara_weight[destination_x + 4][destination_y - 4] = 8
    ara_weight[destination_x - 4][destination_y - 4] = 8
    ara_weight[destination_x + 2][destination_y + 6] = 8
    ara_weight[destination_x - 2][destination_y + 6] = 8
    ara_weight[destination_x + 2][destination_y - 6] = 8
    ara_weight[destination_x - 2][destination_y - 6] = 8
    ara_weight[destination_x + 6][destination_y + 2] = 8
    ara_weight[destination_x - 6][destination_y + 2] = 8
    ara_weight[destination_x + 6][destination_y - 2] = 8
    ara_weight[destination_x - 6][destination_y - 2] = 8
    ara_weight[destination_x + 8][destination_y] = 8
    ara_weight[destination_x - 8][destination_y] = 8
    ara_weight[destination_x][destination_y + 8] = 8
    ara_weight[destination_x][destination_y - 8] = 8
except IndexError:
    gotdata = 'null'


def loc():
    global loca;
    print(loca)


def move_for(x, d):  # x number of blocks   d direction
    ##the hardawre code here
    print("moved ", x, " blocks to the front");
    if d == 0:  # direction 0 up 1 down 2 right 3 left
        loca[1] = loca[1] + x;
    if d == 1:
        loca[1] = loca[1] - x;
    if d == 2:
        loca[0] = loca[0] + x;
    if d == 3:
        loca[0] = loca[0] - x;


def move_back(x, d):
    # the hardware code here

    # write the code of the move to the back function where x is the number of blocks
    # and d is the direction of the car 0 front , 1 back , 2 right , 3 left
    pass;


def rotate_left():
    global direct;
    # the hardware code
    direct = 3;


def rotate_right():
    global direct;
    # the hardware code
    direct = 2;


def rotate_front():
    global direct;
    # the hardware code
    direct = 0;


def rotate_back():
    global direct;
    # the hardware code
    direct = 1;


def see(sensor):
    pass;
    # hardware code here
    # if find some thing return true else return false
    # three sensors one on the front and the second to he right and the third to the left


###################################
# def your_algorithm
########################################

print('*'*20)
i=0
for row in ara_weight:
    print("ara_weight: ", ara_weight[i])
    i+=1
for i in range(len(sum_ara)):
    print(sum_ara[i])
    i+=1
print('*'*20)


# print(loca)
# print(direct)
# move_for(2, direct);
# rotate_right();
#
# print(loca);
#
# print(direct)
while loc() != loca:
    if(ara_weight[loc()+1][loc()] < loc()):
        if(see() == True):
            rotate_front()
            my_location = loc() + 1
            move_for(my_location)
    elif(ara_weight[loc()][loc()+1] < loc()):
        if(see() == True):
            rotate_right()
            my_location = loc() + 1
            move_for(my_location)
    elif(ara_weight[loc()-1][loc()] < loc()):
        if(see() == True):
            rotate_back()
            my_location = loc() + 1
            move_for(my_location)
    elif(ara_weight[loc()][loc()-1] < loc()):
        if(see() == True):
            rotate_left()
            my_location = loc() + 1
            move_for(my_location)