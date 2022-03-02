# 15650 N과 M 2
# 1부터 N까지 중복없이 M개를 고른 수열
# 고른 수열의 내용이 오름차순이어야 함

#%%
N, M = list(map(int, input().split()))
visited = [False] * N
out = []

def back_tracking(depth, N, M):
    if depth == M:
        print(' '.join(list(map(str, out))))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
        if (out != []) and (out[-1] < i+1): # 오름차순으로 숫자를 넣기 위해 조건 추가
            out.append(i+1)
            back_tracking(depth+1, N, M)
            visited[i] = False
            out.pop()
        if out == []:                       # 숫자가 하나도 없는 경우
            out.append(i+1)
            back_tracking(depth+1, N, M)
            visited[i] = False
            out.pop()

back_tracking(0, N, M)
# %%
