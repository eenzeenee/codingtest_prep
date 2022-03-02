# 15649 N과 M 다시 풀기

#%%

N, M = list(map(int, input().split()))
visited = [False] * N
out = []

def back_tracking(depth, N, M):
    if depth == M:                              # 탈출 조건 : back_tracking 함수를 M만큼 반복했다면
        print(" ".join(list(map(str, out))))
        return
    for i in range(len(visited)):
        if not visited[i]:                      #### 여기도 틀림 : 탐사하지 않은 숫자라면 (동일 숫자 반복을 방지하기 위함)
            visited[i] = True                   # 탐사 했음을 확인
            out.append(i+1)                     # 탐사 내용 추가
            back_tracking(depth+1, N, M)        # 깊이 우선 탐색 진행
            visited[i] = False                  # 깊이 우선 탐색 완료
            # out = [] *** 여기가  틀림
            out.pop()                           # 탐색 완료한 내용 제거

back_tracking(0, N, M)

# 시작 정점에서부터 특정 경로를 따라 가능한 멀리 있는 정점을 재귀적으로 먼저 방문하는 방식을 의미한다. 
# 더 방문할 정점이 존재하지 않으면 다시 뒤로 돌아가 다른 경로를 찾아간다.
# %%
