#rent house#

alpha=int(input("tell us the no of floor: "))
beta=int(input("tell us the houses: "))
sum=0
for row1 in range(1,alpha+1): 
    for row2 in range(1,beta+1):
        rent=int(input("bring the rent: "))
        if row2==2 or row2==4:
            if rent>=8000:print("thanks for the payment");sum+=rent
            else:print("need to pay")
        elif row2==1 or row2==3:
            if rent>=6000:print("thanks for the payment");sum+=rent
            else:print("need to pay")
print("total collection: ",sum)
