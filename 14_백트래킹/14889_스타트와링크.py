# 스타트와 링크

#%%
from itertools import combinations
N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
pos_teams = []
min_gap = 1000000

for team in list(combinations(members, N//2)):
    pos_teams.append(team)

for i in range(len(pos_teams) // 2):
    team = pos_teams[i]
    start_stat = 0
    for j in range(N//2):       ## start 팀 : N//2명
        member = team[j]
        for k in team:
            start_stat += stats[member][k]  ## member가 k선수와 함께할 때의 능력치
    team = pos_team[-1-i]
    link_stat = 0
    for j in range(N//2):       ## link 팀 : N//2명
        member = team[j]
        for k in team:
            link_stat += stats[member][k]
    min_gap = min(min_gap, abs(start_stat - link_stat))

print(min_gap)