def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(array)
print("Reversed Array:", reversed_array)

# Alternatively, using slicing
array2 = [10, 20, 30, 40, 50]
reversed_array2 = array2[::-1]
print("Reversed Array using slicing:", reversed_array2)

# Alternatively, using the built-in reverse() method
array3 = [100, 200, 300, 400, 500]
array3.reverse()
print("Reversed Array using reverse() method:", array3)