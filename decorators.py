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

########### end ################