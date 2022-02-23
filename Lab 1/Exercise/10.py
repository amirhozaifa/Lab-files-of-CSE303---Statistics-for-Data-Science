a = [1, 2, 3, 4, 5]

largest = a[0]

for x in a:
    if x > largest:
        largest = x

second_largest = -1

for x in a:
    if x != largest and x > second_largest:
        second_largest = x

print(second_largest)