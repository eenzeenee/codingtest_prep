## 소수 구하기

#%%
input_list = input().split(' ')
M = int(input_list[0])
N = int(input_list[-1])

for i in range(M, N + 1):
    if (i % 2 == 0) and (i != 2):
        pass
    elif (i % 3 == 0) and (i != 3):
        pass
    elif (i % 5 == 0) and (i != 5):
        pass
    else:
        num = 0
        for j in range(2, i + 1):
            if i % j == 0:
                num += 1
                if num > 2:
                    pass
    
        if (i == 2) or (i == 3) or (i == 5) or (num == 1):
            print(i)
    
### 시간초과...
### For문 아닌 다른 방식의 해결책 필요함


# %%
## 에라토스테네스의 체
## 2 이상의 n을 선택하여 그 배수를 모두 제거하는 방식

M, N = map(int, input().split())    #### int() 아니라 int로 넣어서 map해야 함

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):     
            #### x의 제곱근까지 계산하여 그 중에 약수가 있다면 소수 아님
            if x % i == 0:
                return False
        return True

for i in range(M, N + 1):   
    if isPrime(i):
        print(i)


# %%
