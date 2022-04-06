#%%
def solution(name):
    alphas = list(enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    answer = 0
    for t in name:
        for i, alpha in alphas:
            if alpha == t:
                if t == name[0]:
                    if i <= 13:
                        answer += i
                    else:
                        tmp = 25 - i + 1
                        answer += tmp
                elif t == 'A':
                    pass
                else:
                    answer +=1
                    if i <= 13:
                        answer += i
                    else:
                        tmp = 25 - i + 1
                        answer += tmp
                    
    return answer
## 정답률 33.3%
## A 넘어가는 방법 다시 생각해봐야 할 필요 있음

#%%
def solution(name):
    alphas = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx, answer = 0, 0
    
    while True:
        answer += alphas[idx]
        alphas[idx] = 0
        
        if sum(alphas) == 0:
            break
        
        left, right = 1, 1
        while alphas[idx - left] == 0:
            left += 1
        while alphas[idx + right] == 0:
            right += 1
        
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right

    return answer

## A가 몇개 연속되어 있을 때 왼쪽으로 이동할 지, 오른쪽으로 이동할 지 선택해야 함
## 바꿔야하는 알파벳 (A 제외한 알파벳)이 나올때 까지 좌우 방향 전환 거리를 구한 후 최솟값을 나타내는 방향으로 전환
## 모든 알파벳이 계산된 뒤 while 문 나와서 결과 반환

# 정확성 74%......