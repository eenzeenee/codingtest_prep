#%%
# 모범답안 : any 사용하여 코드 간결화

def solution(priorities, location):       
    tmp = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        num = tmp.pop(0)
        if any(num[1] < p[1] for p in tmp):
            tmp.append(num)
        else:
            answer += 1
            if num[0] == location:
                return answer

#%%
# 런타임에러 발생
def solution(priorities, location):
    idxs = [i for i in range(len(priorities))]
    answer = 0
    
    while True:
        p = priorities.pop(0)
        i = idxs.pop(0)
        
        if max(priorities) > p:
            priorities.append(p)
            idxs.append(i)
        else:
            answer += 1
            if i == location:
                return answer


#%%
def solution(priorities, location):
    answer = 1              ## 미리 1 넣어줘서 elif 문으로 break 뽑아냄
    docs = list(range(len(priorities)))
    while priorities:
        top = priorities.pop(0)
        doc = docs.pop(0)
        if len(priorities) == 0:
            break
        if top < max(priorities):
            priorities.append(top)
            docs.append(doc)
        elif doc == location:
                break
        else:
            answer += 1
    return answer