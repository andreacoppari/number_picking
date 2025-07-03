import math

def sequence(n):
    '''
    Prints the first N numbers that produce a symmetric number picking distribution 
    '''
    seq = []
    total = 8
    for _ in range(0, n):
        digits = math.floor(math.log10(total + 2))
        step = 10 ** digits
        total += step
        seq.append(total)
    return seq

print(sequence(100))