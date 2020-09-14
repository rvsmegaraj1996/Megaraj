balance=[200000,19000,3400,10999]
def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money,"debit")
        return balance[pos]
    else:print("cannot debit")
hai=debit(10000,3)
print(hai)


