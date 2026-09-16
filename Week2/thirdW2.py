def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a Number: "))
if n <= 1:
    print("Enter Number Greater than 1")
for i in range(2, n):
    if prime(i):
        print(i)