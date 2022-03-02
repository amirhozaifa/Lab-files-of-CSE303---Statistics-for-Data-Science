# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
a = list({i for i in range(1, 1001) for j in range(2,10) if i % j == 0})
print(a)