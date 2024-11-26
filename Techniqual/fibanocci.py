# Q-Write a Python program to generate Fibonacci numbers up to n

def fibanocci(n):
    a,b = 0,1
    while a < n:
        print(a,end=" ")
        a,b = b,b+a


fibanocci(10)