T = int(input())
for _ in range(T):
    w1, w2 = input().split()
    sort_w1 = sorted(list(w1))
    sort_w2 = sorted(list(w2))
    if sort_w1 == sort_w2 :
        print(f'{w1} & {w2} are anagrams.')
    else:
        print(f'{w1} & {w2} are NOT anagrams.')
