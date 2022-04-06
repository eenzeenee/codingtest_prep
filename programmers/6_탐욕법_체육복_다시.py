#%%
def solution(n, lost, reserve):
    set_l = set(lost) - set(reserve)
    set_r = set(reserve) - set(lost)
    for i in set_r:
        if i+1 in set_l:
            set_l.remove(i+1)
        elif i-1 in set_l:
            set_l.remove(i-1)
            
    return n - len(set_l)

## 테스트 11, 13, 14, 15, 16 실패


#%%
def solution(n, lost, reserve):
    set_l = set(lost) - set(reserve)
    set_r = set(reserve) - set(lost)
    for i in set_r:
        if i-1 in set_l:
            set_l.remove(i-1)
        elif i+1 in set_l:
            set_l.remove(i+1)
            
    return n - len(set_l)

## 보다 작은 숫자인 i-1 부터 삭제하게끔 코드 수정 후 정답 처리됨
## 탐욕법 ~ 가장 작은 숫자부터 차례대로 실행하는 것이 필요함