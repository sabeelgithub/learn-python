def outer(x):
    def inner(y):
        def deep(z):
            return x + y + z
        return deep
    return inner

out = outer(2)
inn = out(3)
print(inn(4))
        