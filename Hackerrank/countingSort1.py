def countingSort(arr):
    # Initialize a frequency array of size 100 (since the values are between 0 and 99)
    frequency = [0] * 100

    # Count the frequency of each element in arr
    for num in arr:
        frequency[num] += 1

    return frequency


# Example usage:
arr = [1, 1, 3, 2, 1]
result = countingSort(arr)
print(result)  # Output: [0, 3, 1, 1, 0, 0, ..., 0] (length of 100)
