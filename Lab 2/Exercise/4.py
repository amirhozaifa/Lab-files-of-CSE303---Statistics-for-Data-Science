# 4. Remove all of the vowels in a string (use string above)
def filter_consonant(c):
    """Returns True if c is a consonant."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    if c in vowels:
        return False
    else:
        return True


s = ""
for x in filter(filter_consonant, "Practice Problems to Drill List Comprehension in Your Head."):
    s += x
print(s)