n = int(input("Enter a  Number: "))

if n == 0:
    print("1")
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(fact)