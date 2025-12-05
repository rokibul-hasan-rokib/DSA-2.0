def second_largest_element(arr):
    if len(arr) < 2:
        return None  # Not enough elements for second largest

    first = second = float('-inf')

    for number in arr:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None

arr = [10, 20, 4, 45, 99]
result = second_largest_element(arr)
print("Second largest element is:", result)