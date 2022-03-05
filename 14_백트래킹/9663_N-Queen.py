# 9663 N-Queen
## N x N 크기의 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
## 각 행마다 퀸은 하나씩 반드시 존재해야 함
## 대각선, 상하로 겹치지 않도록 

# %%
# N = int(input()) ## 시간초과
import sys
N = int(sys.stdin.readline())
rows = [0] * N
answer = 0
visited = [False] * N   # 열 겹치는지 확인하기 위해

def check_attack(x):    # 대각선 겹치는지 확인하기 위해
    for i in range(x):
        
        if abs(rows[x] - rows[i]) == abs(x - i):    ## ** (x-i) 절대값 **
            return False
    return True

def queen(x):
    global answer
    if x == N:
        # print(rows)   # attack 불가능한 모든 경우의 수 확인 위해 출력
        answer += 1
        return
    for i in range(N):      # ** N만큼 재귀 돌기!!!!! queen을 N개 배치해야 하므로!! **
        if visited[i]:  # i번째 열에 queen 있는 경우 continue (아래 명령문 건너뛰고 i+1로)
            continue
        rows[x] = i
        if check_attack(x):
            visited[i] = True
            queen(x+1)
            visited[i] = False  # 시작하는 queen의 열이 동일한 경우를 확인하기 위해 방문 기록을 다시 False로 풀어주는 것
        
queen(0)
print(answer)
# %%

##### 문제 해설 #####
import sys
N = int(sys.stdin.readline())
visited = [False] * N
rows = [0] * N
answer = 0

## 공격 가능한 경우의 수 있는지 확인하기 위한 함수 (공격 가능하면 False, 공격 불가능 하면 = queen을 위치할 수 있다면 True)
def check_attack(x):        
    for i in range(x):      # x열 이전까지의 열에 대해 공격 가능한 위치가 있는지 확인
        if abs(rows[i] - rows[x]) == abs(i - x):    # 열 - 열 / 행 - 행 의 절대값이 같으면 대각선에 위치
            ## 상하 확인하지 않는 이유 : 위의 visited 변수를 활용하여 동일한 열에 queen 추가하지 못하도록 미연에 방지함
            ## 좌우 확인하지 않는 이유 : 모든 행에 queen은 반드시 하나씩 들어가야 하므로
            return False
    return True

## queen의 모든 가능한 배열의 수 찾는 함수
def Queen(x):   # x : queen을 배치하고자 하는 열의 위치
    global answer   # 미리 정의해 둔 변수를 재귀함수를 통해 그 값을 조정하고 싶은 경우 전역변수
    if x == N:      # 모든 열을 다 돈 경우
        answer += 0 # 해당 경우의 수는 공격 불가한 경우이므로 answer에 1 더하기
        return

    for i in range(N):  # 모든 열을 다 돌지 않은 경우 ~ 모든 열을 다 돌리기 위해
        if visited[i]:  # i번째에 이미 queen을 위치한 경우 -> 상하 확인에 걸리므로 검사하지 않음
            continue
        rows[x] = i     # x번째 위치에 queen 배치

        if check_attack(x): # 그 이전 모든 배치들이 이번 배치에 대해 공격이 불가능한 경우라면
            visited[i] = True   # i번째 열을 방문했다고 치고
            Queen(x+1)          # 다음 열에 queen 배열하기
            visited[i] = False  # 배열 가능한 열을 확인했다면 확인한 열은 다시 풀어주기 (모든 재귀를 완료하고 그 경우의 수를 마칠 때 = 새로운 경우의 수 시작할 때)

Queen(0)    # 0번째 열부터 차례대로 queen 배치 시작
print(answer)
        
