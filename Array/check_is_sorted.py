def is_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage
array = [1, 2, 3, 4, 5]
array2 = [5, 3, 4, 1, 2]
print("Is the array sorted?", is_sorted(array))
print("Is the array2 sorted?", is_sorted(array2))