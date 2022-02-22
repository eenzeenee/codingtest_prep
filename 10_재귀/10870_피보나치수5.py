# 피보나치 수 5

#num = int(input())
#%%

num = int(input())

def fibo(x):
    if x > 1:
        return fibo(x-1) + fibo(x-2)
    elif x == 1:
        return 1
    else:
        return 0

print(fibo(num))
# %%
