a = int(input("Enter a Number: "))
orig = a
rev = 0
while a > 0:
    rem = a % 10
    rev = rev*10 + rem
    a //= 10
if orig == rev:
    print("Number is Palindrome.")
else:
    print("Number is not Palindrome.")