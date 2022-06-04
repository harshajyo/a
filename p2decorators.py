import time
def decor(f):
    def wrapper(*args,**kwargs):
        st = time.clock()
        print('started at ',st)
        ret=f(*args,**kwargs)
        et = time.clock()
        print('ended at',et)
        print("time taken ",et-st)
        return ret
    return wrapper

@decor
def add(a,b):
    r=a+b
    print(r)

@decor
def mult(a,b):
    r=a*b
    print(r)

@decor
def pwr(a,b):
    r=a**b
    print(r)

add(10,20)
mult(25,10)
pwr(9,5)

