#%%
def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        scoville.sort()
        try:
            min1 = scoville.pop(0)
            min2 = scoville.pop(0)
            scoville.append(min1 + min2*2)
        except IndexError:
            return -1
        answer += 1
    return answer

### 시간 초과
### 정렬을 while 문 돌때마다 진행 -> 효율성 떨어짐