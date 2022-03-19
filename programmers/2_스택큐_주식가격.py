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