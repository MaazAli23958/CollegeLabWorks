l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

for i,j in zip(l1, reversed(l2)):
    print(f"l1 = {i} and l2 = {j}")