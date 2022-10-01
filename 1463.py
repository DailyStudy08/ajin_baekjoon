N = int(input())
num = [0]*10001
idx = 1
try:
    for i in range(666, 10000000):
        a = str(i)
        if '666' in str(i):
            num[idx] = i
            idx += 1
except:
    pass

print(num[N])
