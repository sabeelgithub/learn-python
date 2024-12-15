"""
Q - Order this dictionary 
    d = {
        "d":1,
        "g":5,
        "c":33
    }
"""

# ans
d = {
        "d":1,
        "g":5,
        "c":33
    }
e=dict(sorted(d.items(), reverse=True))
e=dict(sorted(d.items(), key = lambda item : item[1], reverse=True))
print(e)