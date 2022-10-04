import sys

def partition(left,right):
    p = lst[left]
    i, j = left, right
    while i <= j:
        while i <= j and lst[i] >= p:
            i += 1
        while i <= j and lst[j] <= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[left], lst[j] = lst[j], lst[left]
    return j

def quick_sort(l, r):
    if l < r:
        s = partition(l, r)
        quick_sort(l, s-1)
        quick_sort(s+1, r)

lst = list(map(int, list(sys.stdin.readline().strip())))
quick_sort(0, len(lst)-1)
print(*lst,sep='')