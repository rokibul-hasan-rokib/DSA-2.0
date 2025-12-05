def find_max_min(arr):
    if not arr:
        return None, None

    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_number, min_number = find_max_min(arr)
print(f"Maximum number: {max_number}, Minimum number: {min_number}")

print(f"Max: {max(arr)}, Min: {min(arr)}")