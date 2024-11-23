def factorial(n):
    if n == 1:  # base case
        return n
    else: # recursive case
        return n * factorial(n-1)


s=factorial(4)
print(s)