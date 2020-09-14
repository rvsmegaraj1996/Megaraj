#long jump event between 10 people
person=1;high=0
while person<=20:
    meter=float(input("Enter the jumped distance: "))
    if meter>high:
        high=meter
    person+=1
else:
    print("Event over")
print("The winner is: ",high)


