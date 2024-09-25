#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    firstValue = arr[0]
    secondValue = arr[1]
    thirdValue = arr[2]
    fourthValue = arr[3]
    fifthValue = arr[4]

    arr.remove(arr[0])
    sumOfFour = sum(arr)

    arr.append(firstValue)
    arr.remove(arr[0])
    sumOfThree = sum(arr)

    arr.append(secondValue)
    arr.remove(arr[0])
    sumOfTwo = sum(arr)

    arr.append(thirdValue)
    arr.remove(arr[0])
    sumOfOne = sum(arr)

    arr.append(fourthValue)
    arr.remove(arr[0])
    sumOfZero = sum(arr)

    arr.append(fifthValue)
    arr.remove(arr[0])
    sumOfFive = sum(arr)

    print(min(sumOfOne, sumOfTwo, sumOfThree, sumOfZero, sumOfFour, sumOfFive),
          max(sumOfOne, sumOfTwo, sumOfThree, sumOfZero, sumOfFour, sumOfFive))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
