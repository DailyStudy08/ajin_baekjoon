W = input()

C = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in C:
    W = W.replace(i,'a')
print(len(W))