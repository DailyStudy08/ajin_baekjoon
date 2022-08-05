N = input()
cnt= 0
if len(N) == 1:
    num = '0'+N
else:
    num = N

while True:
    if len(N)==1:
        N ='0'+N
   
    else:
        N = N
        
    a = str(int(N[0]) + int(N[1]))

    b = N[-1] + a[-1]
    cnt += 1

    if b == num:
        print(cnt)
        break
    else:
        N = b
