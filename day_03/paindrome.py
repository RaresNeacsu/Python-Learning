def palindrome(s):
    placeholder=s.lower()
    return placeholder == placeholder[::-1]

s=input("Enter a string: ")
if palindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")