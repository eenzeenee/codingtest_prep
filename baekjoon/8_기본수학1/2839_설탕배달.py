# 설탕 배달

# %%
N = int(input())
answer = 0

if N % 5 == 0:              # 5로 나누었을 때 나머지 값에 대해 각각의 경우의 수 확인
    print(N // 5)
elif N % 5 == 1:
    if N - 6 >= 0:
        print((N - 6) // 5 + 2)
    else:
        print(-1)
elif N % 5 == 2:
    if N - 12 >= 0:
        print((N - 12) // 5 + 4)
    else:
        print(-1)
elif N % 5 == 3:
    if N - 3 >= 0:
        print((N - 3) // 5 + 1)
    else:
        print(-1)
else:
    if N - 9 >= 0:
        print((N - 9) // 5 + 3)
    else:
        print(-1)
