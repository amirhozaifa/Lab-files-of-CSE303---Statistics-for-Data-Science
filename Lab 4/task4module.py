def mean(a):
    """Computes mean from iterable"""
    sum = 0
    for x in a:
        sum += x
    return sum / len(a)