#neasted loop

#bus ticket checking

for bus in range(1,4):
    for seat in range(1,11):
        fare=int(input("Tell us amount: "))
        if fare>=350:
            print("you can travel @",bus,"seat of",seat)
        else:
            print("you are not suppose to")

