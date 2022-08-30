N = int(input())
D = int(input())
lst = [int(input()) for _ in range(N-1)]

cnt = 0
if N == 1:
    print(0)
else:
    while D <= max(lst):
        a = max(lst)
        lst.remove(a)
        a -= 1
        cnt += 1
        D += 1
        lst.append(a)

    print(cnt)

