import sys
L, R = map(int, sys.stdin.readline().split())
minV = 10
for i in range(L, R+1):
    if str(i).count('8')==0:
        print(0)
        break
    else:
        minV = min(minV, str(i).count('8'))
else:
    print(minV)

