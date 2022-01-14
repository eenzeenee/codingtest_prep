# 벌집

A = int(input())
n = 1
i = 0
while True:
    if A - 1 - 6 * i <= 0:
        print(n)
        break
    else:
        i += n
        n += 1