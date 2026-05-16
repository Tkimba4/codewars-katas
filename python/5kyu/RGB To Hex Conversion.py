def rgb(r, g, b):
    h = ""
    for d in [r, g, b]:
        if d < 0 : d = 0
        if d > 255 : d = 255
        h += hex(d)[2:].upper().zfill(2)
    return h
