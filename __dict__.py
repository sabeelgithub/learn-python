
"""
A built-in Python attribute that stores all attributes of an object instance
"""
class Floor:
    def __init__(self):
        self.x = 10
        self.y = 20

f = Floor()
print(f.__dict__)
print(hasattr(f,"__dict__"))
