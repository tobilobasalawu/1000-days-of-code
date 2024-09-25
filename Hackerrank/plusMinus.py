def plusMinus(arr):
    # Write your code here
    length = n
    pos = []
    neg = []
    zero = []
    for i in arr:
        if i == 0:
            zero.append(i)
        elif i < 1:
            neg.append(i)
        else:
            pos.append(i)

    print(len(pos) / length)
    #return len(neg) / length
     #len(zero) / length


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)