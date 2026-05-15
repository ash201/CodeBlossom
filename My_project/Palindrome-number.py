num = int(input("Enter the number: "))
original = num
rev = 0


while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print(original, rev)
if original == rev:
    print("The number is a palindrome")
else:
    print("Not a palindrome")