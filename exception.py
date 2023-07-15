# exception 
a = 5
b = 2

try:
    print('opened resource')
    print(a/b)
    k= int(input('enter a number:'))
    print(k)
   
    
except ZeroDivisionError as e:
   
    print('divisio by zero not possible',e)
except ValueError as e:
    print('invalid input')
except Exception as e:
    print(e)
    
finally:
    print('closed resource')

# exception end