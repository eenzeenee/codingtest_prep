# 소수 찾기

#%%
N = int(input())
answer = 0

inputs = input().split(' ')     #### input을 한번에 받음

for i in inputs:
    i = int(i)
    if i == 1:
        pass
    elif i == 2:
        answer += 1
    else:
        num = 0
        for j in range(2, i+1):
            if i % j == 0:
                num += 1
        if num == 1:
            answer += 1
print(answer)

# %%
