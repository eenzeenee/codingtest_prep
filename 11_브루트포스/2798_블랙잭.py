# 블랙잭

## 브루트포스 : 비교 대상 문자열을 끝까지 비교하거나, 패턴을 찾을때까지 반복해서
## 문자를 하나씩 차례로 비교

#%%
# 원본 문자열에서 패턴이 속한 시작 위치를 반환하기

def bruteforce(pattern, text):
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        print(i, j)
        if text[i] != pattern[j]:
            i -= j
            j = -1  # 다시 처음으로 돌아가서 검색해야 함
        i += 1
        j += 1
    if j == len(pattern):
        return i - len(pattern)
    else:
        return -1
pattern = 'Python'
text = 'Pello Python World'

print(bruteforce(pattern, text))
# %%
N, M = map(int, input().split())
nums = input().split()

answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if int(nums[i]) + int(nums[j]) + int(nums[k]) > M:
                pass
            else:
                answer = max(answer, int(nums[i]) + int(nums[j]) + int(nums[k]))

print(answer)
# %%
