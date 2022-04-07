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
        # 비교적 적은 수의 이동을 더하기
        if left < right:
            answer += left
            idx -= left     # idx 이동시키기
        else:
            answer += right
            idx += right    # idx 이동시키기

    return answer

## A가 몇개 연속되어 있을 때 왼쪽으로 이동할 지, 오른쪽으로 이동할 지 선택해야 함
## 바꿔야하는 알파벳 (A 제외한 알파벳)이 나올때 까지 좌우 방향 전환 거리를 구한 후 최솟값을 나타내는 방향으로 전환
## 모든 알파벳이 계산된 뒤 while 문 나와서 결과 반환

# 정확성 74%......

#%%
def solution(name):
    answer = 0
    min_left_right = len(name)  # 왼쪽에서 오른쪽으로만 이동할 때
    next_idx = 0

    for idx, char in enumerate(name):
        answer += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)

        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        min_left_right = min(min_left_right, idx + idx + len(name) - next_idx)
        # idx + idx + len(name) - next_idx : 오른쪽으로 이동했다가 왼쪽으로 다시 이동하는 경우
        # min_left_right : 왼쪽에서 오른쪽으로 한 방향으로만 이동하는 경우
        ## 둘을 비교하여 작은 수만 이동수로
    answer += min_left_right

    return answer
## 또 실패..

#%%
#%%  해설... 이해해보자...
def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]    # 왼쪽에서 오른쪽으로
        right_moved = name[i:]+name[:i]     # 오른쪽에서 왼쪽으로 -> 왼쪽에서 오른쪽으로
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1     # 커서 이동 횟수
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)     # 알파벳 이동 횟수

            answer = min(answer, row_move + col_move)

    return answer
# 성공