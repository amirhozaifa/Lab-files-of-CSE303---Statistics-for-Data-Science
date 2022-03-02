# 5. Find all of the words in a string that are less than 5 letters (use string above)
def filter_alpha(x):
    if(x.isalpha()):
        return True
    else:
        return False
    
    
s = "Practice Problems to Drill List Comprehension in Your Head."
words = []
for word in s.split():
    t = ""
    for c in filter(filter_alpha, word):
        t += c
    words.append(t)

print([word for word in words if len(word) < 5])
