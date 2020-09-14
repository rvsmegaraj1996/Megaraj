#conrol statement : if...if...if...else
#theme park

amt=int(input("Enter the amount to get ticket: "))
if amt >=920:
    print("Enjoy the day with black thunder")
    weight=float(input("Enter the weight: "))
    if weight>=45 and weight<60:
        print("you can enjoy waves games")
    if weight>=50 and weight<80:
        print("you can enjoy rapid river")
    if weight>=80 and weight<120:
        print("you can enjoy roller coaster")
    if weight>=60 and weight<100:
        print("you can enjoy in swimmping pool")
    else:
        print("you can enjoy all sort of dry games")
else:
        print("insufficient amount")
