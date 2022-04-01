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