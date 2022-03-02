# N과 M (1)
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
