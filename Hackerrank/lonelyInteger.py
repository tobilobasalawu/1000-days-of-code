def lonelyinteger(a):
    # Write your code here
    unique = 0
    for num in a:
        unique ^= num

    print(unique)

lonelyinteger([0,0,1,2,1])