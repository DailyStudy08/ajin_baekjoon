N = int(input())
def data(n):
    cnt = 0
    if n < 100: #100보다 작은 수 는 모두 한수
        return n
    else:
        for i in range(100,n+1): #100 이상의 수는 문자열로 만들고 리스트로 만들고 다시 숫자로 만든다
            lst = list(map(int,str(i)))  
            a= lst[0]-lst[1] # 첫번째와 두번째 수의 차
            for j in range(1,len(lst)-1): #두번째와 세번째의 차 부터 검사해서 a와 같지 않다면 break
                if lst[j]-lst[j+1] != a:
                    break
            else: # break 없이 끝났다면 한수 이므로 카운트증가
                cnt+=1
        return cnt+ 99 # 100 미만 한수 개수 + 100이상 한수 개수
print(data(N))
