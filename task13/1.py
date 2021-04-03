t=int(input("enter the no. of test cases:"))
if 1<=t<=100000:
    for i in range(0,t):
        a=int(input("enter the range:"))
        if 1<=a<=1000000000:
            c=0
            for j in range(1,a):
                    if j%5==0 or j%3==0:
                        c+=j
            print(c)
        else:
            print("invalid")
else:
    print("invaild")
