# train ticket


for seat in range(1,11):
    pay=int(input("Enter the amount: "))
    if pay>=180:
        age=int(input("tell us your age: "))
        if age>=55 or age<=10:
            print("half of payment is fine so remaining is: ",(pay-90))
        else:
            print("remaining is: ",(pay-180))
        print("seat is booked",seat)
    else:
            print("insufficient amount")

'''
seat=1
while seat<=10:
    pay=int(input("Enter the amount: "))
    if pay>=180:
        age=int(input("tell us your age: "))
        if age>=55 or age<=10:
            print("half of payment is fine so remaining is: ",(pay-90))
        else:
            print("remaining is: ",(pay-180))
        print("seat is booked",seat)
        seat+=1
    else:
            print("insufficient amount")
'''
