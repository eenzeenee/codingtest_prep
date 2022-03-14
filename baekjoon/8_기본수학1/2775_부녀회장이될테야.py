# 부녀회장이 될테야
#%%
T = int(input())
for _ in range(T):
    k = input()
    n = input()             ### 입력이 한줄씩 들어온다... 잘 보고 풀기

    zero = [i+1 for i in range(int(n))]
    for _ in range(int(k)):
        for i in range(1, int(n)):
            zero[i] += zero[i-1]
    print(zero[-1])
# %%

# %%
