# 정수 삼각형
#%%
n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
# %%
print(nums)
# %%
answer = 0

for i in range(len(nums)):
    if i == 0:
        answer += nums[i][0]
        k = 0
    else:
        if nums[i][k] >= nums[i][k+1]:
            answer += nums[i][k]
        else:
            answer += nums[i][k+1]
            k += 1

print(answer)
### 바로 아래층에서 제일 큰 수를 더함 ~ 이거 아님!!
### 모든 수의 합이 최대가 되도록!!
# %%
nums = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
#%%

for i in range(1,len(nums)):
    for j in range(i+1):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        elif j == i:
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j], nums[i-1][j-1])
print(max(nums[-1]))
# %%
## 최종 제출
n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
    
for i in range(1,len(nums)):
    for j in range(i+1):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        elif j == i:
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j], nums[i-1][j-1])
print(max(nums[-1]))
# %%
