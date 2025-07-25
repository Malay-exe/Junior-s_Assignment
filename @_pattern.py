def pat(x):
    for i in range(x):
        for j in range(x+1):
            if j==x-i or j==x:
                print("@",end='')
            else:
                print(" ",end='')
        print("\n")
x=4
(pat(x))