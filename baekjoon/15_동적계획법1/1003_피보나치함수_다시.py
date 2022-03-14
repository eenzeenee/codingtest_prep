# 피보나치 함수

#%%

def fibonacci(n):
    if n == 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(3)
# %%
N = int(input())
for _ in range(N):
    num = int(input())
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]

    for i in range(2, num+1):
        cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
        cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
    print(cnt_0[num], cnt_1[num])


# %%
