w = input().upper()
dic = {}

for i in w:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


a = sorted(dic.items(), key = lambda x : x[1], reverse=True)

if len(a) > 1:
    if a[0][1] == a[1][1]:
        print('?')
    else:
        print(a[0][0])
else:
    print(a[0][0])