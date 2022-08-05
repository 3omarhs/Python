r = int(input("Enter the number of rows:"))
for i in range (r, 0 ,-1):
    n = i
    for j in range(0, i):
        print(n, end='')
    print("\r")