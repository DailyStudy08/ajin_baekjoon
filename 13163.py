N = int(input())
for _ in range(N):
    data = list(input().split())
    data.pop(0)
    print('god',end='')
    print(*data,sep='')
