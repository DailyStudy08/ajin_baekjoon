H, M = map(int,(input().split()))

if M > 44:
    M = M-45
    H = H
else :
    M = 60+M-45
    if H == 0:
        H = 23
    else:
        H = H-1

print(H,M)