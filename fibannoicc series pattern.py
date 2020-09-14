#fibonocci series pattern
num1,num2=0,1
for row in range(4,0,-1):
    for col in range(1,5):
        if col>=row:
            if row==4:
                print(num1,end=" ")
            elif row==3 and col==3:
                print(num2,end=" ")
            else:
                sum=num1+num2
                num1=num2;
                num2=sum;
                print(sum,end=" ")
            print("#",end=" ")
        else:print(end=" ")
    print()
    
    
#fibbonocci floid with numbers

num=1
for row in range(1,5):
    for space in range(4-1,row-1,-1):print(" ",end=" ")
    for data in range(1,row+1):
        print(num,end=" ")
        if row%2==0:num+=2
        else:num+=1
    print()
   
#fibbonocci pattern wit data
num=1;limit=1
fix=int(input("tell us bound: "))
for row in range(1,fix+1):
    for space in range(fix-1,row-1,-1):print(" ",end="")
    for data in range(1,limit+1):
        print(num,end="")
        if row%2==0:num+=2
        else:num+=1
    limit+=2;print()

