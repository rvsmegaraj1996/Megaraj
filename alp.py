'''
ABCDE
FGHIJ
KLMNO
PQRST
UVWXY
'''
for row in range(1,6):
    for alp in range(1,6):
        if alp%2==0:
            print(A,end=" ");alp+=26
        else:
                print(Z,end=" ");alp+=26
    print()
        
