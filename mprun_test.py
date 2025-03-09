from math import pi

def plocha_kruhu(polomer: int) -> int:
    return pi * (polomer ** 2)

def secti_vsechny_plochy(args) -> int:
    suma_ploch = 0
    for polomer in args:
        suma_ploch += plocha_kruhu(polomer)
    
    return suma_ploch
