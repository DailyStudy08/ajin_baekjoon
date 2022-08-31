N = int(input())
lst =[input() for i in range(N)]

lst.sort()

d={}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i]=1
maxV = max(d,key=d.get)
print(maxV)
