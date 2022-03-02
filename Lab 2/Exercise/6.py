# 6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)
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

lens = {word: len(word) for word in words}
print(lens)