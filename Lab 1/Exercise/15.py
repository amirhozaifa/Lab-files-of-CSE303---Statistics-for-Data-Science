a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = []

for x in a:
    if x%2 != 0:
        c.append(x)
        
for x in b:
    if x%2 == 0:
        c.append(x)
        
print(c)