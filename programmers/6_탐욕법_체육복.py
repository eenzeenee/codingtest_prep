#%%
def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in reserve:
        for j in lost:
            if i - 1 == j or i + 1 == j:
                lost.remove(j)
                answer += 1
                break
    return answer

## test 2/3/5/7/12/13/18 실패

#%%

def solution(n, lost, reserve):
    answer1 = n - len(lost)
    answer2 = n - len(lost)
    for i in lost:
        if i-1 in reserve:
            answer1 += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer1 += 1
            reserve.remove(i+1)
    for i in lost:
        if i+1 in reserve:
            answer2 += 1
            reserve.remove(i+1)
        elif i-1 in reserve:
            answer2 += 1
            reserve.remove(i-1)
    return max(answer1, answer2)

## test 3, 7, 12, 13, 14 실패

#%%

"""여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다."""

def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_lost:
        if i-1 in set_reserve:
            set_lost.remove(i)
        elif i+1 in set_reserve:
            set_lost.remove(i)
    return n - len(set_lost)

# 실패 다수 발생

#%%
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)

## 문제 해결 완료