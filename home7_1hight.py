import math
def size_square(size):
    perimeter = size * 4
    diagonal  = math.sqrt(2*size**2)
    square   = size**2
    return perimeter,diagonal,square
print(size_square(7))
