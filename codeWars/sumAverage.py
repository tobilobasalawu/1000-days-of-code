from math import floor
def sum_average(arr):
    ans = []
    for i in arr:
        average = sum(i)/len(i)
        ans.append(average)
    return floor(sum(ans))

