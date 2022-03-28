#%%
def solution(citations):
    answer = 0
    n = len(citations)
    for i in range(n, -1, -1):
        cite_up = 0
        cite_down = 0
        for h in citations:
            if h >= i:
                cite_up += 1
            if h <= i:
                cite_down += 1
        if cite_up >= i:
            answer = i
            break
    return answer