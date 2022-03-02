# 8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
a = {i: j for i in range(1, 1001) for j in range(2,10) if i % j == 0}
print(a)