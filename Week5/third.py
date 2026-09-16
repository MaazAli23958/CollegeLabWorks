import random
import string

uppercase = random.choice(string.ascii_uppercase)
uppercase2 = random.choice(string.ascii_uppercase)
digit = random.choice(string.digits)
special = random.choice("@#$%")
characters = string.ascii_letters + string.digits + "@#$%"
password = uppercase + uppercase2 + digit + special

for i in range(6):
    password += random.choice(characters)
    
print(f"Password =  {password}")