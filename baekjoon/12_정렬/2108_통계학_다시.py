# 2108 통계학

#%%
import sys
N = int(input())

nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))
    # nums.append(int(input()))

# 산술평균
print(round(sum(nums) / N))

# 중앙값
nums.sort()
print(nums[N//2])

# 최빈값
from collections import Counter

cnts = Counter(nums).most_common(2)
if N <= 1:
    print(cnts[0][0])
else:
    if cnts[0][1] != cnts[1][1]:
        print(cnts[0][0])
    else:
        print(cnts[1][0])

# 범위
print(nums[-1] - nums[0])