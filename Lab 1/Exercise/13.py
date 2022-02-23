s = input("Enter string: ")

t = "CSE303"
count = 0

for i in range(len(s)):
    u = s[i:i + len(t)]
    if u == t:
        count += 1
print(count)