x = input("enter ascending(s) or descending(d)..")
if(x == 'ascending'):
    y = int(input("enter a number.."))
    for i in range(0,y,1):
        print(i)
elif(x == 'descending'):
    y = int(input("enter a number.."))
    for i in range(y, 0, 1):
        print(i)
else:
    print('error, wrong input!')