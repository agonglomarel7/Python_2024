
dic = {"x":4,"y":7}

def add(x,y):
    return x+y

print(add(**dic))

ls=[4,7]

def times(x,y):
    return x*y

print(times(*ls))

def som(*args):
    print(args)
    total=0
    for arg in args:
        total +=arg
    
    return total

print(som(1,4,5))