import sys

H, W = map(int,sys.stdin.readline().split())

cloud = [sys.stdin.readline().strip() for _ in range(H)]



for j in cloud:
    stack =[]
    cnt = 0
    for i in j:
        if  i == '.':
            if stack :
                stack.append(i)
            else:
                print(-1,end=' ')
        
        else:
            if stack:

                while stack:
                    stack.pop()
                    print(cnt,end=' ')
                    cnt += 1
                stack.append(i)
                cnt = 0

            else:
                stack.append(i)
    while stack:
        stack.pop()
        print(cnt,end=' ')
        cnt += 1
    print()