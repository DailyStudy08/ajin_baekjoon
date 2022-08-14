lst = [0,0,'ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
W = input()
cnt = 0
for i in W:
    for j in range(2,len(lst)):
        if i in lst[j]:
            cnt += j+1
print(cnt)
