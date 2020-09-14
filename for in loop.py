#for in loop
required=[12,"aravind",98,4,10.3,"gopi"]
print(len(required))

#while statement

init=2
while init<len(required)-1:
    print(required[init])
    init+=1


#for in range


for index in range(0,len(required)-3):
    print(required[index])


#for in loop

for data in required:
    print(data)
