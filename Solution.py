arr = [1 , 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31, 37, 41, 43, 47, 53, 59]
q = int(input())
for i in range(q):
    n = int(input())
    m = 1
    for i in range(len(arr)):
        m *= arr[i]
        if m > n:
            print(i  - 1)
            break
