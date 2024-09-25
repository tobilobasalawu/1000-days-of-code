from itertools import count
from operator import index


def sum_of_intervals(intervals):
    result = []
    count = 0
    answer = 0
    #intervals = str(intervals)
    for char in intervals:
        result.append(char[1]-char[0])
        for i in result:
            #count += 1
            if i > 1:
                answer = i
                result.remove(i)
            elif i < 0:
                answer += i
    return answer

print(sum_of_intervals([(1, 5), (1,3)]))
