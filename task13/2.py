import math
t=int(input("enter the no. of test cases:"))
if 1<=t<=math.pow(10,5):
    for i in range(0,t):
        n=int(input("enter the range:"))
        if 10<=n<=4*math.pow(10,16):
            e1=2
            b=0
            e=0
            c=2
            while e<n:
                e=4*e1+b
                b=e1
                e1=e
                c+=e
            print(c-e)
        else:
            print("invalid")
else:
    print("invalid")
