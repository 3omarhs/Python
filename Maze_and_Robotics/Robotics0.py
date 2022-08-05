import numpy

# to convert from dgree to rad (x/180)*pi
# O1 and O2 are the variables of the 2 DoF system
O1 = 60
d2 = 5
O3 = 30
d4 = 5

O1 = (O1 / 180) * numpy.pi
O3 = (O3 / 180) * numpy.pi

print(O1)
print(O3)

a1 = 5  # cm
a2 = 5
a3 = 5
a4 = 5
a5 = 5

I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
I = numpy.matrix(I)

R2_1 = [[numpy.cos(O3), -numpy.sin(O3), 0], [numpy.sin(O3), numpy.cos(O3), 0], [0, 0, 1]]
R2_1 = numpy.matrix(R2_1)
R2_1 = numpy.dot(I, R2_1)
print("second frame")
print(R2_1)

R3_2=[[0,0,1],[-1,0,0],[0,1,0]];  ## Depends on the direction of movement
R3_2=numpy.matrix(R3_2);
R3_2=numpy.dot(R3_2,I);
print("first frame")
print("\n")
print(R3_2)

R4_3 = [[numpy.cos(O3), -numpy.sin(O3), 0], [numpy.sin(O3), numpy.cos(O3), 0], [0, 0, 1]]
R4_3 = numpy.matrix(R4_3)
R4_3 = numpy.dot(I, R4_3)
print("second frame")
print(R4_3)

R5_4 = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
R5_4 = numpy.matrix(R5_4)
R5_4 = numpy.dot(R5_4, I)
print("third frame")
print(R5_4)

dv2_1 = [[a2 * numpy.cos(O1)], [a2 * numpy.sin(O1)], [a1]]
dv2_1 = numpy.matrix(dv2_1)
print(dv2_1)

dv3_2 = [[a4 * numpy.cos(O3)], [a4 * numpy.sin(O3)], [a3]]
dv3_2 = numpy.matrix(dv3_2)
print(dv3_2)

dv4_3 = [[0], [0], [a3 + d4]]
dv4_3 = numpy.matrix(dv4_3)
print(dv4_3)

dv5_4 = [[0], [0], [a4 + d4]]
dv5_4 = numpy.matrix(dv5_4)
print(dv5_4)

#############################################################################
H2_1 = numpy.concatenate((R2_1, dv2_1), axis=1)
H2_1 = numpy.concatenate((H2_1, [[0, 0, 0, 1]]), axis=0)
print("first homo")
print(H2_1)

H3_2 = numpy.concatenate((R3_2, dv3_2), axis=1)
H3_2 = numpy.concatenate((H3_2, [[0, 0, 0, 1]]), axis=0)
print("second homo")
print(H3_2)

H4_3 = numpy.concatenate((R4_3, dv4_3), axis=1)
H4_3 = numpy.concatenate((H4_3, [[0, 0, 0, 1]]), axis=0)
print("third homo")
print(H4_3)



H5_4 = numpy.concatenate((R5_4, dv5_4), axis=1)
H5_4 = numpy.concatenate((H5_4, [[0, 0, 0, 1]]), axis=0)
print("second homo")
print(H5_4)

H5_1 = numpy.dot(H2_1, H3_2)
H5_1 = numpy.dot(H5_1, H4_3)
H5_1 = numpy.dot(H5_1, H5_4)



H5_1 = numpy.matrix(H5_1)

print("final location and orientation of the 2DoF arm is")
print(H5_1)

print("\n\n\n\n\n")



# Omar Hassan Al-Jammal 201910155
input("press enter to exit..")
