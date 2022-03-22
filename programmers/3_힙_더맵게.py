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

#%%
def solution(scoville, K):
    import heapq
    answer = 0
    while min(scoville) < K:
        heapq.heapify(scoville)
        try:
            min1 = scoville.pop(0)
            min2 = scoville.pop(0)
            scoville.append(min1 + min2*2)
            
        except IndexError:
            return -1
        answer+=1
    return answer

# 시간 초과 여전 + 실패 발생

#%%

def solution(scoville, K):
    import heapq
    answer = 0
    while min(scoville) < K:
        heapq.heapify(scoville)
        try:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2*2)
            
        except IndexError:
            return -1
        answer+=1
    return answer

# 시간 초과 여전히 발생

#%%

import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()                     #### sort를 먼저해서 가장 작은 수가 제일 앞에 오도록
    while scoville[0] < K:              #### min 함수 대신 인덱스를 사용하여 가장 앞의 가장 작은 수를 찾기 (속도 개선됨!!)
        if len(scoville) == 1:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min1 + min2*2)

        answer+=1
    return answer