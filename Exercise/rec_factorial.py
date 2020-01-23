def rec_factorial(a):
    if a==1:
        return a
    else:
        return rec_factorial(a-1) * a