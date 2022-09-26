import string
import sys

def solution(n, t, m, p):
    answer = ''
    result = ''    # 10진수를 n진수로 바꾼 결과를 담을 변수
    num = 0        # 0부터 부를거니까
    n = int(n)
    t = int(t)
    m = int(m)
    p = int(p)

    # result의 길이가 t(튜브가 말할 숫자 갯수)*m(참가 인원) 보다 작은 동안
    # num 을 1씩 증가하며 n진수로 바꿔서 result에 담아준다.
    while len(result) < t*m:
        change_num = str(convert_recur(num, n))
        result += change_num
        num += 1

    # result에서 튜브가 말 할 숫자 뽑아서 answer에 담기
    for i in range(len(result)//m):
        answer += result[i*m+p-1]
        if len(answer) == t:
            break
    return answer, result, num


# 10진수 num을 n진수로 바꾸는 함수
def convert_recur(num, n):
    # number = '0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, n)
    return convert_recur(q, n) + number[r] if q else number[r]

n = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

print(solution(n, t, m, p))