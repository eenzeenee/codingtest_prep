# 파도반 수열

#%%

T = int(input())
l = [0] * 101
l[1] = 1
l[2] = 1
l[3] = 1


for _ in range(T):
    N = int(input())
    for i in range(4, N+1):
        l[i] = l[i-3] + l[i-2]
    print(l[N])
# %%
