# 15651 N과 M 3
# 1부터 N까지 중복없이 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨

#%%
N, M = list(map(int, input().split()))
visited = [False] * N
out = []

def back_tracking(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return                      #### return 까먹지 말기
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = False
            out.append(i+1)
            back_tracking(depth+1, N, M)
            visited[i] = False
            out.pop()

back_tracking(0, N, M)


# %%
