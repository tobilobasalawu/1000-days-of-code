def diagonalDifference(arr):
    n = len(arr)
    left_to_right = 0
    right_to_left = 0

    for i in range(n):
        left_to_right += arr[i][i]
        right_to_left += arr[i][n - i - 1]

    return abs(left_to_right - right_to_left)


# Example usage:
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

result = diagonalDifference(arr)
print(result)  # Output: 2
