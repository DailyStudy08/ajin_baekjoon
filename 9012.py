import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    data = sys.stdin.readline().strip()
    stack = []
    for d in data:
        if d == '(':
            stack.append(d)
        elif d == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')