########## decorator #############
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)



def smart_sub(func):
    def inner(c,d):
        if c < d:
            c,d = d,c
        return func(c,d)
    return inner

@smart_sub
def sub(c,d):
    print(c-d)

sub(1,2)

import time

def time_calculataion(func):
    def wrapper(*args,**kwargs):
        star_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__} is {end_time - star_time}")
        return result
    return wrapper
@time_calculataion
def sleep_check():
    time.sleep(5)
    return "Function Completed"

sleep_check()

########### end ################