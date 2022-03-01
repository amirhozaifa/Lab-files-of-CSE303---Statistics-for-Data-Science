def compound_interest_2019_3_60_109(p, r, t):
    """Returns compound interest."""
    return p * (1 + r / 100) ** t


p = int(input("Enter principal amount: "))
r = int(input("Enter interest rate: "))
t = int(input("Enter time (in years): "))
print(compound_interest_2019_3_60_109(p, r, t))
