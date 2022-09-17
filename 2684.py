coin = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
P = int(input())
for _ in range(P):
    case = input()
    for c in coin:
        cnt = 0
        for i in range(38):
            a = case[i:i+3]
            if a == c:
                cnt += 1
        print(cnt,end=' ')
    print()

