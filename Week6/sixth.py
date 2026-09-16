string = input("Enter any String: ")
uppercase = 0
lowercase = 0
alphabets = 0
digits = 0

for ch in string:
    if ch.isupper():
        uppercase += 1
    if ch.islower():
        lowercase += 1
    if ch.isalpha():
        alphabets += 1
    if ch.isdigit():
        digits += 1

print(f"Number of Uppercase Characters: {uppercase}")
print(f"Number of Lowercase Characters: {lowercase}")
print(f"Total Number of Alphabets: {alphabets}")
print(f"Total Number of Digits: {digits}")