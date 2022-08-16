price_dict = {'package':[],'piece':[]}
N, M = map(int,input().split())
for i in range(M):
    pack , pi = map(int,input().split())
    price_dict['package'] += [pack]
    price_dict['piece'] += [pi]

a, b = divmod(N, 6)

cnt = 0
if min(price_dict['piece'])*6 <= min(price_dict['package']):
    cnt += min(price_dict['piece'])*N

elif min(price_dict['piece'])*6 > min(price_dict['package']):
    if min(price_dict['piece'])*b <= min(price_dict['package']):
        cnt += min(price_dict['package'])*a + min(price_dict['piece'])*b
    if min(price_dict['piece'])*b > min(price_dict['package']):
        cnt += min(price_dict['package'])*(a+1)
print(cnt)

