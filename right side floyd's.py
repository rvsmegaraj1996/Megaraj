#right side floyd's

for row in range(1,6):
    for space in range(4,row-1,-1):
        print(" ",end="")
    for data in range(1,row+1):
        print("*",end="")
    print()


for row in range(5,0,-1):
    for col in range(1,6):
        if col>=row:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()
