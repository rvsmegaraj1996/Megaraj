def demo():
    exp=int(input("tell us experience: "))
    skill=input("tell us skill ")
    if exp>=4 and exp<6 and skill == 'python' or skill=='java':
       return "promoted as team lead"
    elif exp>=6 and exp<10 and skill == 'aglie' or skill=='developer':
        return "promoted as project manager"
    return "Be as associate"
desig=demo()
print(desig)
                
