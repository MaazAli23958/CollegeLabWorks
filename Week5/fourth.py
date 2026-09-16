l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
l2 = [10, 15, 20, 25, 30, 35, 40, 50]

res = []

for i in l1:
    if i % 2 != 0:
        res.append(i)

for i in l2:
    if i % 2 == 0:
        res.append(i)
        
print(res)