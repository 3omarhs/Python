import numpy

def forword(O1, O2, a1, a2, a3, a4):
    O1=(O1/180)*numpy.pi;
    O2=(O2/180)*numpy.pi;

    I=[[1,0,0],[0,1,0],[0,0,1]];
    I=numpy.matrix(I);
    R2_1=[[numpy.cos(O1), -numpy.sin(O1), 0], [numpy.sin(O1), numpy.cos(O1), 0], [0,0,1]];
    R2_1=numpy.matrix(R2_1);
    R2_1=numpy.dot(I,R2_1);
    #print("first frame");
    #print("\n");
    #print(R2_1);
    R3_2=[[numpy.cos(O2), -numpy.sin(O2), 0], [numpy.sin(O2), numpy.cos(O2), 0], [0,0,1]];
    R3_2=numpy.matrix(R3_2);
    R3_2=numpy.dot(I,R3_2);
    #print("second frame");
    #print(R3_2);
    R3_1=numpy.dot(R2_1,R3_2);
    #print("final oriantation");
    #print(R3_1);
    dv2_1=[[a2*numpy.cos(O1)],[a2*numpy.sin(O1)],[a1]];
    dv2_1=numpy.matrix(dv2_1);
    #print(dv2_1);

    dv3_2=[[a4*numpy.cos(O2)],[a4*numpy.sin(O2)],[a3]];
    dv3_2=numpy.matrix(dv3_2);
    #print(dv3_2);

    H2_1=numpy.concatenate((R2_1,dv2_1), axis=1);
    H2_1=numpy.concatenate((H2_1,[[0,0,0,1]]), axis=0);
    #print(H2_1);
    H3_2=numpy.concatenate((R3_2,dv3_2), axis=1);
    H3_2=numpy.concatenate((H3_2,[[0,0,0,1]]), axis=0);
    #print(H3_2);
    H3_1=numpy.dot(H2_1,H3_2);
    #print("final location and orientation of the 2DoF arm is");
    #print(H3_1);
    s1 = H3_1
    # print("X = ",H3_1[0,3])
    # print("Y = ",H3_1[1,3])
    # print("Z = ",H3_1[2,3])
    print("X = ", H3_1[0, 3], "     ", end='')
    print("Y = ", H3_1[1, 3], "     ", end='')
    print("Z = ", H3_1[2, 3], "     ")
    return [H3_1[0, 3], H3_1[1, 3], H3_1[2, 3]]

def inverse(x, y, z, a1, a2, a3, a4):
    r = numpy.sqrt((x * x) + (y * y))
    d = ((r * r) - (a2 * a2) - (a4 * a4)) / (-2 * a2 * a4)
    E = numpy.arccos(d)
    O1 = (180 - E)/10
    print("First angle: ", int(O1))
    E2 = numpy.arccos(((a2 * a2) - (r * r) - (a4 * a4)) / (-2 * r * a4))
    E3 = numpy.arctan(y / x)
    O2 = E3 - E2
    O2 = (O2 / numpy.pi) * 180
    print("Second angle: ", int(O2))



O1=int(input("Enter the first angle: "))
O2=int(input("Enter the second angle: "))
a1=int(input("Enter the first arm length in CM: "))   #cm
a2=int(input("Enter the second arm length in CM: "))
a3=int(input("Enter the third arm length in CM: "))
a4=int(input("Enter the fourth arm length in CM: "))

# forword(9, 17, 5, 5, 5, 5)
print("forword  kinematics:")
str = forword(O1, O2, a1, a2, a3, a4)
print("inverse  kinematics:")
inverse(str[0], str[1], str[2], a1, a2, a3, a4)