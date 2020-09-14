#pyramid
'''
n=8
limit=1
for row in range(1,n+1):
    for space in range(n-1,row-1,-1): print(" ",end="")
    for data in range(1,limit+1): print("*",end="")
    limit+=2;print()
'''

n=int(input("tell us how many rows you wish:"))
limit=1
for row in range(n,0,n+1):
    
    
    for space in range(n-1,row-1,-1):print(" ",end="")
    for data in range(1,limit+1):print("*",end="")
    limit+=2;print()
