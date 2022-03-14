# 계단 오르기

#%%
import sys 
# input = sys.stdin.readline 
arr = [] 
dp = []

l = int(input())
for _ in range(l):
    arr.append(int(input()))            ## append : python에서는 시간복잡도 O(1)

dp.append(arr[0])                            # 0번째까지의 최대 가중치
dp.append(arr[0] + arr[1])                   # 1번째까지의 최대 가중치
dp.append(max(arr[0]+arr[1], arr[1]+arr[2])) # 2번째까지의 최대 가중치

for i in range(3, l):
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1]))
    print(dp)

print(dp[-1])

## 마지막 계단을 기준으로
## 마지막 하나 전 계단을 밟았으면 마지막 두개 전 계단은 밟으면 안됨
## 마지막 두개 전 계단을 밟았으면 그 이전 계단은 신경쓰지 않아도 됨
### 그 중 가장 큰 수를 더하면 됨

## i번째 계단의 가중치 합
### -> i-2번째 계단까지의 최대 가중치 합 + 현재 i번째 계단의 가중치
### -> i-3번째 계단까지의 최대 가중치 합 + i-1번째 계단의 가중치 + 현재 i번째 계단의 가중치
# %%
