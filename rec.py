#jio recharge
recharge=10
while recharge<=100:
    pay=int(input("Enter the amount: "))
    if pay>=1200:
        cust=int(input("which plan using: "))
        if cust>=100 or cust<=55:
            print("remaining people is top only: "(pay-2020))
        else:
                print("remaining pepole using net and fulltalktime package only:",(pay-1500))
        print("how many recharge in one day",recharge)
        recharge+=1
    else:
            print("insufficient amount")
            
