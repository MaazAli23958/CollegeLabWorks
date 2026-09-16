n = int(input("Enter a Number: "))
count = 0
while n > 0:
    rem = n % 10
    count = count +1
    n //= 10
print(f"Total No. of Digits are {count}")