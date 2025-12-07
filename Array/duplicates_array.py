def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
array = [1, 2, 2, 3, 4, 4, 5]
print("Array after removing duplicates:", remove_duplicates(array))