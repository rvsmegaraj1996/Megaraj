#flash sale
turns=int(input("Tell us how many times you wish open the sales: "))
for one in range(1,turns+1):
    stock=int(input("tell us stock for the sale: "))
    qty=0
    for time in range(1,31):
        required=int(input("tell us how many quantity you want: "))
        if required<=stock:
            stock-=required
            print("your order of",required,"is placed @",one)
            qty+=required
        if stock<=0 or time==30:
            print("sale is over");break
    print(one,"sold items are",qty)
