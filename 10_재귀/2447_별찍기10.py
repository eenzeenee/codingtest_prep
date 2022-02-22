# 별 찍기 10

# %%

def stars(star):   
    matrix = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:                      # 3으로 나눈 몫이 1일 때 : 가운데 비우도록 " " * len(n)
            matrix.append(star[i % len(star)] + ' ' * len(star) + star[i % len(star)])
        else:                                        # 3으로 나눈 몫이 1이 아닌 경우 : 가운데 비우지 않고 3배
            matrix.append(star[i % len(star)] * 3)
    return matrix

N = int(input())
n = 0
star = ['***', '* *', '***']

while N > 3:
    N = int(N / 3)
    n += 1

for i in range(n):
    star = stars(star)

for i in star:
    print(i)
# %%
