def diagonalDifference(arr):
    leftD = arr[0][0] + arr[1][1] + arr[2][2]
    rightD = arr[0][2] + arr[1][1] + arr[2][0]

    return abs(leftD - rightD)

print(diagonalDifference([[-1,1,-7,-8], [-10, -8, -5, -2], [0, 9,7, -1], [4,4,-2,1]]))