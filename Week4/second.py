def func(l):
    for i in l:
        if l[0] == l[length-1]:
            return True
    return False

l = [1, 2, 4, 5, 34, 35, 24, 1]
length = len(l)
result = func(l)
print(result)