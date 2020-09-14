#relational and logical operator
#control if else
#bigger among three strings
dev1=input('tell developer1: ')
dev2=input('tell developer2: ')
dev3=input('tell developer3: ')
if dev1>dev2 and dev3:
    print(dev1,'is bigger than',dev2,'and',dev3)
elif dev2>dev3:
    print(dev2,'is bigger than',dev1,'and',dev3)
else:
    print(dev3,'is bigger than',dev1,'and',dev2)
