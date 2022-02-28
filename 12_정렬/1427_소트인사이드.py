# 1427 소트인사이드

#%%
num = list(map(int, list(input())))
num.sort()

answer = 0

for i in range(len(num)):
    answer += num[i] * 10 ** (i)

print(answer)
# %%
