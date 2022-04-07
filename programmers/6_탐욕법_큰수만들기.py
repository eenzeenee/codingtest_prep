#%%
def solution(number, k):
    from itertools import combinations
    nums = [int("".join(i)) for i in combinations(number, len(number)-k)]
    
    answer = str(max(nums))
    return answer
# 시간초과

#%%