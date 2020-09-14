#Atm denominations
two=3;five=10;hun=50;temp=0;cash=0;state=""
cash=int(input("Tell us required amount: "))
if two>0:
    temp=cash//2000
    if two>=temp:
        cash-=(temp*2000)
        two-=temp
        state+=str(temp)+" X 2000\n"
    else:
        cash-=(two*2000)
        state+=str(two)+" X 2000\n"
        two=0
    if five>0:
        temp=cash//500
        if five>=temp:
            cash-=(temp*500)
            five-=temp
            state+=str(temp)+" X 500\n"
    else:
        cash-=(five*500)
        state+=str(five)+" X 500\n"
        five=0
    if hun>0:
        temp=cash//100
        if hun>=temp:
            cash-=(temp*100)
            hun-=temp
            state+=str(temp)+" X 100\n"
            hun=0
    if(cash==0):
        print(state)
    else:
        print("insufficent of dispense")
