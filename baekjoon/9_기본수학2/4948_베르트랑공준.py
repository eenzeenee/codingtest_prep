# 베르트랑 공준

#%%
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    n2_nums = [isPrime(x) for x in range(2*n+1)]
    n_nums = n2_nums[:n]
    print(sum(n2_nums) - sum(n_nums))

#### 시간초과...

# %%

#### 제한된 범위 (1 <= n <= 123456)내의 소수를 저장하고
#### for문을 돌리는 동안 소수 리스트에 있는 소수들을 꺼내오는 방식으로

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

all_list = list(range(2,123456*2))  #### 주어진 범위의 소수 저장하기 위해 범위 설정
primes = []                         #### 소수 저장을 위한 리스트 생성

for i in all_list:
    if isPrime(i):
        primes.append(i)            #### 주어진 범위 내 소수 모두 저장

while True:
    n = int(input())
    answer = 0
    if n == 0:
        break
    for i in primes:                #### 주어진 범위 내 소수에서 순환하도록
        if n < i <= 2*n:
            answer += 1
    print(answer)

# %%
