import sys

cnt = 0 
while True :
    n = int(sys.stdin.readline())
    if n == 0:
        break

    name = [sys.stdin.readline().strip() for i in range(n)]

    lst1 = sum([sys.stdin.readline().split() for i in range(2*n-1)],[])
    for num in lst1:
        if lst1.count(num) == 1 and num.isnumeric():
            cnt += 1
            print(cnt ,name[int(num)-1])
