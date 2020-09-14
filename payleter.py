#filpkart pay leter limit eligibility check for 15
for customer in range(21,36):
    worth=int(input("tell us cumulative amount of your orders: "))
    if worth>=30000 and worth<=50000:
        print("pay leter limit is 6000")
    elif worth>=50001 and worth<=75000:
        print("pay leter limit is 8000")
    elif worth>=75001 and worth<=100000:
        print("pay leter limit is 150000")
    elif worth>=150001:
        print("pay leter limit is 25000")
    else:
        print("sorry you are not eligible to pay leter")
