# 어떤 과학자가 발표한 논문 n편 중, 
# h번 이상 인용된 논문이 h편 이상이고 
# 나머지 논문이 h번 이하 인용되었다면 
# h의 최댓값이 이 과학자의 H-Index입니다.

#%%
def solution(citations):
    answer = 0
    n = len(citations)
    for i in range(n, -1, -1):      # n : 가능한 최대 인용 수 (모든 논문의 인용 횟수가 n인 경우)
        h = i
        cite_up = 0                 # h 이상으로 인용된 논문 수
        cite_down = 0               # h 이하로 인용된 논문 수
        for j in citations:
            if j >= h:
                cite_up += 1
            if j <= h:
                cite_down += 1
        #print(h, ":", end = ' ')
        #print(cite_up, cite_down)
        if cite_up >= h:     # h번 이상 인용된 논문이 h편 이상
            answer = h
            break
    return answer