def rec_multiply(a,b):
    if a==1:
        return b

    else:
        return rec_multiply(a-1,b) +b


