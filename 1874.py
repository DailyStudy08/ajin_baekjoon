stack = [0]
n = int(input())
m = 1
result = []
for i in range(n):
    num = int(input())
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        while m <= num:
            stack.append(m)
            result.append('+')
            m += 1
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            break
else:
    print(*result, sep='\n')

