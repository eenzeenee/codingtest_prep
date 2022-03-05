# 15652 N과 M 4
# 1부터 N까지 중복없이 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨
# 고른 수열은 비내림차순이어야 함
    # 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순

#%%
N, M = list(map(int, input().split()))
out = []
visited = [False] * N

def back_tracking(depth, N, M):
    if depth == M:
        print(' '.join(list(map(str, out))))
        return
    for i in range(len(visited)):
        if not visited[i]:      ## out 내의 모든 요소가 겹치지 않도록 ; only 내림차순
            if (out != [] and out[-1] < i+1) or (out == []): 
                visited[i] = True
                out.append(i+1)
                back_tracking(depth+1, N, M)
                visited[i] = False
                out.pop()
        if visited[i]:          ## out 내의 요소가 겹쳐도 되는 상황 ; "비"내림차순
            if (out != [] and out[-1] == i+1):
                visited[i] = True
                out.append(i+1)
                back_tracking(depth+1, N, M)
                visited[i] = False
                out.pop()

back_tracking(0, N, M)
# %%
