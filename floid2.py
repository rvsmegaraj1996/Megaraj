'''
2
4 6
8 10 12
14 16 18 20
22 24 26 28 30
'''
mul=2
for row in range(1,6):
    for col in range(2,row+2):
        print(mul,end=" ")
        if row%2==0:mul+=2
        else:mul+=2
    print()
