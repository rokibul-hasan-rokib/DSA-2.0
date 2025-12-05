# Array Traversal

## array_1.1.py - Basic Array Traversal

### Description
This program demonstrates the simplest way to traverse (iterate through) an array in Python using a for loop.

### Concept
Array traversal is the process of visiting each element in an array sequentially. It's one of the fundamental operations you can perform on arrays.

### Code Explanation
```python
arr = [10, 20, 30, 40, 50]

for element in arr:
    print(element, end=" ")

print()  # For a new line after the loop
```

1. **Array Declaration**: Creates an array with 5 elements
2. **For Loop**: Iterates through each element in the array
3. **Print Statement**: Prints each element followed by a space (using `end=" "`)
4. **New Line**: Adds a line break after all elements are printed

### Output
```
10 20 30 40 50
```

### Time Complexity
- **O(n)** - where n is the number of elements in the array

### Space Complexity
- **O(1)** - only using a constant amount of extra space

### Key Points
- Python lists are dynamic arrays
- The for-in loop is the most Pythonic way to traverse an array
- `end=" "` parameter prevents printing each element on a new line
