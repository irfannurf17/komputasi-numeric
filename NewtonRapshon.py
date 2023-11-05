
def func(x):
    y=x**3-x**2+2
    return y

def derifunc(x):
    y=3*x*x-2*x
    return y

c=-10

def newtonrapshon(x):
    h=func(x)/derifunc(x)
    i=0
    while abs(h)>= 0.001:
        i=i+1
        h=func(x)/derifunc(x)
        x=x-h
        print('Iterasi %d nilai x dari persamaan adalah : ' %i, x)
        
newtonrapshon(c)
