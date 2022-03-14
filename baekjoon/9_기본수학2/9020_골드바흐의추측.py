# 골드바흐의 추측
# 2보다 큰 짝수를 2개의 소수의 합으로 나타낼 수 있음

#%%
T = int(input())

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    n1 = n / 2
    n2 = n / 2
    while True:
        if isPrime(n1) and isPrime(n2):
            print(int(n1),int(n2))
            break
        else:
            n1 -= 1
            n2 += 1