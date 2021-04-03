import math
t=int(input("enter the no. of test cases:"))
if 1<=t<=10:
    for i in range(0,t):
        b=int(input("enter the number:"))
        if 10<=b<=math.pow(10,12):
            a=[]
            for num in range(0, b+1):
               if num > 1:
                   for i in range(2, num):
                        if (num % i) == 0:
                           break
                   else:
                        if b%num==0:
                            a.append(num)
            print(max(a))
else:
    print("invalid")
