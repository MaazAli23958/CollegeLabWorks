import numpy as np

arr = np.array([
    [20, 40, 10, 30],
    [4, 2, 6, 2],
    [60, 34, 23, 28],
    [78, 45, 23, 89]
])

result1 = arr[:, arr[1].argsort()]
print(f"Sorted by Second Row: \n{result1}")

result2 = arr[arr[:, 1].argsort()]
print(f"Sorted by Second Column: \n{result2}")