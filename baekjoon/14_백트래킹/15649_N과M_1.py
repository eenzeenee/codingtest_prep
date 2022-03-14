# N과 M (1)
# 백트래킹 : 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 해를 찾아가는 기법 (가지치기)
## 반복문의 횟수를 줄일 수 있어 효과적임
## 답이 될 만한지 판단하고 그렇지 않으면 그 부분까지 탐색하는 것을 하지 않고 가지치기하는 것
## DFS 등으로 모든 경우의 수를 탐색하는 과정에서, 조건문 등을 걸어 답이 절대로 될 수 없는 상황을 정의하고,
## 그러한 상황일 경우 탐색을 중지시킨 뒤 그 이전으로 돌아가 다른 경우를 탐색하게끔
#%%
N, k = list(map(int, input().split()))
visited = [False for _ in range(N)]        # 탐사 여부 체크
out = []                                   # 결과를 저장하기 위한 리스트

def back_tracking(depth, N, k):
    print('depth :', depth)
    if depth == k:                         # 탈출 조건
        print('if', out)
        print(' '.join(map(str,out)))
        return
    for i in range(len(visited)):          # 탐사 check 하면서
        if not visited[i]:                 # 탐사하지 않았다면
            visited[i] = True              # 탐사 시작 (중복 제거)
            out.append(i+1)                # 탐사 내용
            print("out.append(i+1) :", out)
            back_tracking(depth+1, N, k)   # 깊이 우선 탐색
            visited[i] = False             # 깊이 탐사 완료
            out.pop()                      # 탐사 내용 제거
            print('out.pop() :', out)

back_tracking(0, N, k)
# %%
N, k = list(map(int, input().split()))
visited = [False for _ in range(N)]        # 탐사 여부 체크
out = [] 

def back_tracking(depth, N, k):
    if depth == k:
        print(' '.join(map(str, out)))
        return
    for i in range(len(visited)):          # 탐사 check 하면서
        if not visited[i]:                 # 탐사하지 않았다면
            visited[i] = True              # 탐사 시작 (중복 제거)
            out.append(i+1)                # 탐사 내용
            back_tracking(depth+1, N, k)   # 깊이 우선 탐색
            visited[i] = False             # 깊이 탐사 완료
            out.pop()

back_tracking(0, N, k)
# %%
