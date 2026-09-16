import secrets

otp = secrets.randbelow(900000) + 100000
print(f"Your OTP is {otp}")