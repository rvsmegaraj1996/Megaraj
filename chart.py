#theatre chart:$ -

chart=""
for row in range(1,5):
    for seat in range(1,7):
        amt=int(input("tell us amount: "))
        if amt>=300:
            print("ticket booked @ ",row,seat)
            chart+='$'
        else:
            print("insufficient amount")
            chart+='-'
    chart+='\n'
print(chart)
