def palindrome_checker_2019_3_60_109(s):
    """Checks if given string is palindrome"""
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


s = input("Enter string: ")
if palindrome_checker_2019_3_60_109(s):
    print(f'{s} is palindrome')
else:
    print(f'{s} is not palindrome')