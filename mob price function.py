#iteration through recursive
#iteration through loop
mobPrice=[9700,15600,89000,2000,45000,15000,6000]
def iterate(index=0):
    if index==len(mobPrice):return
    else:
        print(mobPrice[index])
        index+=1
        iterate(index)
iterate()
for temp in range(2,len(mobPrice)-1):
    print(mobPrice[temp])
