#%%
def solution(prices):
    answer = [0]*len(prices)
    i = 0
    while True:
        if len(prices) == 1:
            break
        num = prices.pop(0)
        for t in prices:
            if num > t:
                answer[i] += 1      ## 나보다 작으면 1초만 더하고 break으로 반복문 빠져나감
                break
            answer[i] += 1
        i += 1
    return answer
#### 시간초과

#%%
def solution(prices):
    answer = [0]*len(prices)
    i = 0
    while True:
        if i == len(prices):
            break
        num = prices[i]
        for t in prices[i+1:]:
            if num > t:
                answer[i] += 1
                break
            answer[i] += 1
        i += 1
    return answer

### pop 말고 indexing으로 바꿔도 시간 초과...

#%%
def solution(prices):
    answer = [0]*len(prices)
    i = 0
    while True:
        if i == len(prices):
            break
        num = prices[i]
        for t in prices[i+1:]:
            if num > t:
                answer[i] += 1
                break
            answer[i] += 1
        i += 1
    return answer

### while 문을 사용하지 않아도 시간 초과...

#%% 
def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]  ## 남은 시점 저장
    stack = [0]         ## 가격이 하락하지 않은 동안의 인덱스 저장

    for i in range(1, len(prices)):
        while stack:
            idx = stack[-1]
            # print(i, idx)                 # i가 현재 인덱스 / idx가 비교하고자 하는 인덱스
            if prices[idx] > prices[i]:     # 가격이 떨어졌다면,
                answer[idx] = i - idx       # 가격이 떨어지지 않은 동안의 시간 저장
                stack.pop()                 # 가격이 떨어진 인덱스 stack 에서 빼내기
            else:                           # 가격이 떨어지지 않았다면,
                break                       # while 문 빠져나가기
        stack.append(i)                     # stack에 가격이 떨어지지 않은 위치 인덱스 저장하기
    return answer

# %%

### 제출
def solution(prices):
    answer = [len(prices)-1-i for i in range(len(prices))]
    stack = [0]
    
    for i in range(1, len(prices)): # 현재 인덱스
        while stack:
            idx = stack[-1]         # 비교하고자 하는 인덱스
            if prices[i] < prices[idx]:
                answer[idx] = i - idx
                stack.pop()         # stack의 모든 인덱스에 대해 가격이 하락했는지 확인하기 - 하락 안했으면 넘기기
            else:
                break
        stack.append(i)
    
    return answer

# 이중 for 문에서 한번의 for문으로 변경하여 효율성 문제 해결