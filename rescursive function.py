#recursive function:function calling itself
#usage:quit like a loop
def nums(start=1):
    if start==10:
        return
    else:
        print("Hai")
        start+=1
        nums(start)
nums()
