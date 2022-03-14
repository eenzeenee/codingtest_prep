# 1003 피보나치 함수

#%%
import sys
N = int(sys.stdin.readline())

def fibonacci(n):
    global zero_cnt, one_cnt
    if n == 0:
        zero_cnt += 1
        return 0
    elif n == 1:
        one_cnt += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for _ in range(N):

    zero_cnt = 0
    one_cnt = 0

    fibonacci(int(sys.stdin.readline()))
    print(zero_cnt, one_cnt)

#### 시간 초과
#### 피보나치 수열의 원리는 이용하되 카운트를 세는 형식이 아니라 다른 방식으로 접근 필요
# %%
### 0의 출력횟수, 1의 출력횟수 자체를 더하는 방식으로
N = int(input())

for _ in range(N):
    num = int(input())
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    for i in range(2, num+1):
        cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
        cnt_1.append(cnt_1[i-1] + cnt_1[i-2])

    print(cnt_0[num], cnt_1[num])
    ## 마지막 숫자가 아닌 num번째 숫자를 가져오는 이유 : 
    ## 0, 1이 입력으로 들어왔을 때 모두 0 1으로 출력되는 현상을 방지하기 위해

# %%
