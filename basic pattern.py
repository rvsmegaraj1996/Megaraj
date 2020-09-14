'''
#####
#####
#####
#####
#####

'''
for row in range(1,6):
    for sym in range(1,6):
        print('#',end=" ")
    print()


'''
1 5 3 10 5
7 15 9 20 11
13 25 15 30 17
19 35 21 40 23
25 45 27 50 29
'''

mul=5;odd=1
for row in range(1,6):
    for sym in range(1,6):
        if sym%2==0:
            print(mul,end=" ");mul+=5
        else:
            print(odd,end=" ");odd+=2
    print()
