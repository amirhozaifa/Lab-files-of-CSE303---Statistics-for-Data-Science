def prime_find_2019_3_60_109(n):
    """Returns true if n is prime."""
    if n <= 1:
        return False
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True


n = int(input("Enter number: "))
if prime_find_2019_3_60_109(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')