str = input("Enter a string ").strip().lower()
rev = ""
for ch in str:

    rev = ch + rev
print(rev)
if rev == str:
    print("string is palindrome")
else:
    print("Not a Palindrome")      