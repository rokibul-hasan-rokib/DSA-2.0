arr = [10, 20, 30, 40, 50]

for element in arr:
    print(element, end=" ")

print()  # For a new line after the loop

for i in range(len(arr)):
    print(f"Index {i}: {arr[i]}")


for index, value in enumerate(arr):
    print(f"Index {index}: {value}")

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")