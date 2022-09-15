import sys
while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums[0] == 0:
        break
    c = max(nums)
    nums.remove(c)
    if nums[0]**2 + nums[1]**2 == c**2:
        print('right')
    else:
        print('wrong')

