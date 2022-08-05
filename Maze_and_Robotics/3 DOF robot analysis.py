import math

import numpy

#to convert from dgree to rad (x/180)*pi
# O1 and O2 are the variables of the 2 DoF system
O1=60
O2=5
d3=5

O1=(O1/180)*numpy.pi
O2=(O2/180)*numpy.pi

print(O1)
print(O2)

a1=5    #cm
a2=5
a3=5
a4=5

I=[[1,0,0],[0,1,0],[0,0,1]]
I=numpy.matrix(I)

R2_1=[[numpy.cos(O1), -numpy.sin(O1), 0], [numpy.sin(O1), numpy.cos(O1), 0], [0,0,1]]
R2_1=numpy.matrix(R2_1)
R2_1=numpy.dot(I,R2_1)
print("first frame")
print("\n")
print(R2_1)

R3_2=[[numpy.cos(O2), -numpy.sin(O2), 0], [numpy.sin(O2), numpy.cos(O2), 0], [0,0,1]]
R3_2=numpy.matrix(R3_2)
R3_2=numpy.dot(I,R3_2)
print("second frame")
print(R3_2)

R4_3=[[1,0,0],[0,1,0],[0,0,1]];
R4_3=numpy.matrix(R4_3);
R4_3=numpy.dot(R4_3,I);
print("third frame");
print(R4_3);

dv2_1=[[a2*numpy.cos(O1)],[a2*numpy.sin(O1)],[a1]]
dv2_1=numpy.matrix(dv2_1)
print(dv2_1)

dv3_2=[[a4*numpy.cos(O2)],[a4*numpy.sin(O2)],[a3]]
dv3_2=numpy.matrix(dv3_2)
print(dv3_2)

dv4_3=[[0],[0],[a3+d3]]
dv4_3=numpy.matrix(dv4_3)
print(dv4_3)

#############################################################################
H2_1=numpy.concatenate((R2_1,dv2_1), axis=1)
H2_1=numpy.concatenate((H2_1,[[0,0,0,1]]), axis=0)
print("first homo")
print(H2_1)

H3_2=numpy.concatenate((R3_2,dv3_2), axis=1)
H3_2=numpy.concatenate((H3_2,[[0,0,0,1]]), axis=0)
print("second homo")
print(H3_2)

H4_3=numpy.concatenate((R4_3,dv4_3), axis=1)
H4_3=numpy.concatenate((H4_3,[[0,0,0,1]]), axis=0)
print("third homo")
print(H4_3)

H4_1=numpy.dot(H2_1,H3_2)
H4_1=numpy.dot(H4_1,H4_3)
print("final location and orientation of the 2DoF arm is")
print(H4_1)

H4_1=numpy.matrix(H4_1)

print("\n\n\n\n\n")
#############################################################################
X=H4_1[0,3]
Y=H4_1[1,3]
Z=H4_1[2,3]

r= numpy.sqrt((X*X)+(Y*Y))
d=((r*r)-(a2*a2)-(a4*a4))/(-2*a2*a4)

E2 =numpy.arccos(((a2*a2)-(r*r)-(a4*a4))/(-2*r*a4))
E3=numpy.arctan(Y/X)
O2_cal=E3-E2
O2_cal=(O2_cal/numpy.pi)*180
print("O1 = ", O2_cal)

E =numpy.arccos(d)
E=(E/numpy.pi)*180
O1_cal=180-E
print("O2 = ", O1_cal)

y0=(d3+a3)
d3_cal=(y0-a3)
print("d3 = ", d3_cal)