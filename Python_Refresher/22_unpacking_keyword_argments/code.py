
def name(**kwargs):
    
    return (kwargs)


print(name(name="Bob",age=25))

def show_dic(**kwargs):

    for args, val in kwargs.items():
        print(f"{args}: {val}")

show_dic(name="Key",age=23)

def combinaison(*arg,**kwargs):

    print(arg)
    print(kwargs)

combinaison(1,2,4,7,8,name="Emma",age=22,Job="Cyber Analyst")