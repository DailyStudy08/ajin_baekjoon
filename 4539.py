import sys

n = int(sys.stdin.readline().strip()) 
for _ in range(n):
    num = list(map(int,input()))

    for i in range(len(num)-1,0,-1):
        if len(num) == 1 :
            print(num[0])
        else:
            if num[i] >= 5:
                num[i] = 0
                num[i-1] += 1
            else:
                num[i] = 0
                
    for j in num:
        print(j,end='')
    print()

