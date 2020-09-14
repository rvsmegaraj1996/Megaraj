#floid pattern
'''
*
**
***
****
*****
'''

for row in range(1,6):
    for col in range(1,row+1):
        print("*",end=" ")
    print()

'''
1
2 4
6 7 8
9 11 13 15
17 18 19 20 21
'''
data=1
for row in range(1,6):
    for col in range(1,row+1):
        print(data,end=" ")
        if row%2==0:data+=2
        else:data+=1
    print()
