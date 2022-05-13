import math as m

def crc(r: float) -> float:
    """Function for calculating the area of a circle
    parameter: radius
    returns: pi * r^2"""

    if type(r) != type(1) and type(r) != type(1.1):
        raise TypeError
    if r <= 0:
        raise ValueError
    return (m.pi) * float(pow(r,2))

def rct(l: float,w: float) -> float:
    """Function for calculating the area of a rectangle
    parameter 1: width
    parameter 2: height
    returns: width * height"""

    if type(l) != type(1) and type(l) != type(1.1) and type(w) != type(1) and type(w) != type(1.1):
        raise TypeError
    if l <= 0 or w <= 0:
        raise ValueError
    return float(l * w)

def sqr(l: float) ->float:
    """Function for calculating the area of a square
    parameter: side length
    returns: side length * side length"""

    if type(l) != type(1) and type(l) != type(1.1):
        raise TypeError
    if l <= 0:
        raise ValueError
    return float(pow(l, 2))

def trg(b: float, h: float) -> float:
    """Function for calculating the area of a triangle
    parameter 1: base width
    parameter 2: height
    returns: 1/2 * base width * height"""

    if type(b) != type(1) and type(b) != type(1.1) and type(h) != type(1) and type(h) != type(1.1):
        raise TypeError
    if b <= 0 or h <= 0:
        raise ValueError
    return float(0.5 * b * h)
