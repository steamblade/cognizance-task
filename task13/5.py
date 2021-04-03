t=int(input("enter the no. of test cases:"))
if 1<=t<=10:
    for g in range(0,t):
        n=int(input("enter range:"))
        if 1<=n<=40:
            a=[]
            a2=[]
            for num in range(0, n+1):
                if num > 1:
                    for i in range(2, num):
                            if (num % i) == 0:
                                    break
                    else:
                        a.append(num)
            for j in range(0,len(a)):
                a1=[]
                for j1 in range(0, n+1):
                    b1=a[j]*j1
                    if b1<n:
                        a1.append(b1)
                a2.append(max(a1))
            c=1
            for h in a2:
                c=c*h
            print(c)
        else:
            print("invalid")
else:
    print("invalid")
