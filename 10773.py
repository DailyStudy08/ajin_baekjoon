import sys
stack = []
K = int(sys.stdin.readline().strip())
for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num:
        stack.append(num)

    else:
        stack.pop()
print(sum(stack))