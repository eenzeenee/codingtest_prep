# 2231 분해합

#%%
N = int(input())

for i in range(1, N+1):
    num = [int(x) for x in str(i)]
    if i + sum(num) == N:
        print(i)
        break
    else:
        pass
    if i == N:      ## N+1이랑 같을 때가 아니라 N이랑 같을때 답없음
        print(0)
# %%