import sys
sys.stdin = open('4344.txt','r')

C= int(input())

for i in range(C):
    N,*rest= map(int,(input().split()))
    
    avr = sum(rest)/len(rest)
    cnt = 0
    for j in rest:
        if j > avr:
            cnt += 1
    print(f'{(cnt/len(rest)*100):.3f}%')
# (round((cnt/len(rest)*100),3),'%')