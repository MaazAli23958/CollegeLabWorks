string = input("Enter a String: ")
symbols = "@#$"
encrypted = ""

for ch in string:
    encrypted = encrypted + ch + symbols
print("Encrypted: ", encrypted)

decrypted = ""

for i in range(0, len(encrypted), 4):
    decrypted = decrypted + encrypted[i]
print("Decrypted: ", decrypted) 