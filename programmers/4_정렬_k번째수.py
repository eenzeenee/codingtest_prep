#%%
def solution(array, commands):
    t = 0
    answer = [0]*len(commands)
    while True:
        if t == len(commands):
            break
        i, j, k = commands[t]
        arr = array[i-1:j]
        arr.sort()
        answer[t] = arr[k-1]
        t += 1