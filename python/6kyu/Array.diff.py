def array_diff(a, b):
    d = a.copy()
    for i in a:
        if i in b:
            d.remove(i)
        
    return d