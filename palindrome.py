def is_palindrome(s):
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


s = "madam"

if is_palindrome(s):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
