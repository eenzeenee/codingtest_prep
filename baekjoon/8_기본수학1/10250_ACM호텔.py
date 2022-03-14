# ACM 호텔

T = int(input())
result = []
for _ in range(T):
    H, W, N = input().split()
    if int(N) % int(H) != 0:
        F = int(N) % int(H)
        S = int(N) // int(H) + 1

    else:                              ## 순번이 층수로 나누어떨어지는 경우 0층이 되는 경우 방지하기 위해
        F = int(H)
        S = int(N) // int(H)
        
    if S >= 10:
        print(str(F) + str(S))
    else:
        print(str(F) + '0' + str(S))