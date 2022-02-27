# 통계

#%%
import sys

N = int(input())

nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))      ## input 시간초과 방지 위해
#%%

# 산술평균
print(round(sum(nums) / N))

# 중앙값
nums.sort()
print(nums[N//2])

# 최빈값
from collections import Counter
count = Counter(nums).most_common(2)
if len(nums) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

# 범위
print(nums[-1] - nums[0])

#%%

# %%
