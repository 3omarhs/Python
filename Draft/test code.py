import numpy

a1 = 5
a2 = 5
a3 = 5

d1 = 0
d2 = 0
d3 = 0

R2_1 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
R3_2 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
R4_3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

Dv2_1 = [[0], [a1+d1], [0]]
Dv3_2 = [[a2+d2], [0], [0]]
Dv4_3 = [[0], [0], [a1+d1]]

R4_1 = numpy.dot(R2_1,R3_2)
R4_1 = numpy.dot(R4_1,R4_3)

print("final oriantation:")
print(R4_1)

H2_1=numpy.concatenate((R2_1,Dv2_1), axis=1)
H2_1=numpy.concatenate((H2_1,[[0,0,0,1]]), axis=0)

H3_2=numpy.concatenate((R3_2,Dv3_2), axis=1)
H3_2=numpy.concatenate((H3_2,[[0,0,0,1]]), axis=0)

H4_3=numpy.concatenate((R4_3,Dv4_3), axis=1)
H4_3=numpy.concatenate((H4_3,[[0,0,0,1]]), axis=0)

H4_1=numpy.dot(H2_1,H3_2)
H4_1=numpy.dot(H4_1,H4_3)

print("final location and orientation of the 2DoF arm is")
print(H4_1)

input("tap enter to exit...")