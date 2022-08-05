import numpy

#to convert from dgree to rad (x/180)*pi

# O1 and O2 are the variables of the 2 DoF system
file1 = open("test.txt", "a")
file1.write("O1");
file1.write(" "*20);
file1.write("O2");
file1.write(" "*20);
file1.write("X");
file1.write(" "*20);
file1.write("Y");
file1.write("\n");
for loop1 in range(0, 181, 5):
	for loop2 in range(0, 181, 5):
		O1=loop2;
		O2=loop1;

		file1.write(str(O1));
		file1.write(" "*20);

		file1.write(str(O2));
		O1=(O1/180)*numpy.pi;
		O2=(O2/180)*numpy.pi;

		a1=5;    #cm
		a2=5;
		a3=5;
		a4=5;

		I=[[1,0,0],[0,1,0],[0,0,1]];
		I=numpy.matrix(I);

		R2_1=[[numpy.cos(O1), -numpy.sin(O1), 0], [numpy.sin(O1), numpy.cos(O1), 0], [0,0,1]];
		R2_1=numpy.matrix(R2_1);



		R2_1=numpy.dot(I,R2_1);

		print("first frame");
		print("\n");
		print(R2_1);


		R3_2=[[numpy.cos(O2), -numpy.sin(O2), 0], [numpy.sin(O2), numpy.cos(O2), 0], [0,0,1]];
		R3_2=numpy.matrix(R3_2);
		R3_2=numpy.dot(I,R3_2);

		print("second frame");
		print(R3_2);

		R3_1=numpy.dot(R2_1,R3_2);





		print("final oriantation");
		print(R3_1);



		dv2_1=[[a2*numpy.cos(O1)],[a2*numpy.sin(O1)],[a1]];
		dv2_1=numpy.matrix(dv2_1);
		print(dv2_1);



		dv3_2=[[a4*numpy.cos(O2)],[a4*numpy.sin(O2)],[a3]];
		dv3_2=numpy.matrix(dv3_2);
		print(dv3_2);


####################################################


		H2_1=numpy.concatenate((R2_1,dv2_1), axis=1);


		H2_1=numpy.concatenate((H2_1,[[0,0,0,1]]), axis=0);

		print(H2_1);




		H3_2=numpy.concatenate((R3_2,dv3_2), axis=1);


		H3_2=numpy.concatenate((H3_2,[[0,0,0,1]]), axis=0);

		print(H3_2);




		H3_1=numpy.dot(H2_1,H3_2);


		print("final location and orientation of the 2DoF arm is");
		print(H3_1);

		s1 = H3_1
		file1.write(" " * 20);
		file1.write(str(s1[0,3]));
		file1.write(" " * 20);
		file1.write(str(s1[1,3]));
		file1.write("\n");
file1.close();

input("go and open test.txt file...")