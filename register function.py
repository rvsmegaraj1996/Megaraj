#function with default argument
#def fun_name(parameter='')
def register(prefix,name,location="Ms/Miss/Mrs"):
    if location=='salem':print(prefix,name,"has approved in",location)
    elif location=='chennai':print(prefix,name,"has gone under waiting state since its",location)
    else:print("Business not approved")
register("Ms","zealous tech corp","salem")
register("zealous tech corp","salem","Ms")
def register(name,location,prefix="Mr/Miss/Mrs"):
    if location=='salem':print(prefix,name,"has approved in",location)
    elif location=='chennai':
        print(prefix,name,"has gone under waiting state since its",location)
register("MS","zealous tech crop","Salem")
register("Tata automobiles","Chennai","Mr.")
