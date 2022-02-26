# 영화감독 숌

#%%
N = int(input())
start = 666
answer = []
while N > 0:
    num_list = list(str(start))
    for i in range(len(num_list)):
        try:
            if (num_list[i] == num_list[i+1] == num_list[i+2] == '6') and (start not in answer):
                answer.append(start)
                N -= 1
        except:
            pass
    start += 1

print(answer[-1])

