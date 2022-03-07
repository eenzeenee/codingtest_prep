# 스타트와 링크

#%%
# import sys
# N = int(sys.stdin.readline())
# teams = [list(map(int, sys.stdin.readline().split()))]

N = int(input())
teams = [list(map(int, input().split())) for _ in range(N)]
min_gap = 200

def check_gap(depth):
    if depth == 