N = int(input())
student = [input() for _ in range(N)]
n = len(student[0])
for i in range(1,n+1):
    num = set()
    for j in range(N):
        num.add(student[j][-i:]) 
    if len(num) == N:
        print(num)
        print(i)
        break
    
