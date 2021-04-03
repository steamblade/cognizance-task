x=eval(input("enter the coordinate of the friend's house:"))
c=0
print("the minimum number of steps that the elephant needs to make to get from point 0 to point x("+str(x)+"):",end=' ')
while x>0:
    if x>=5:
        x-=5
        c+=1
    elif x==4:
        x-=4
        c+=1
    elif x==3:
        x-=3
        c+=1
    elif x==2:
        x-=2
        c+=1
    elif x==1:
        x-=1
        c+=1
print(str(c))
