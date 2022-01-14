## 손익분기점

# A, B, C = input().split()
# n = 1
# while True:
#     if B > C:
#         n = -1
#         break
#     ex = int(A) + int(B) * n
#     im = int(C) * n
#     if ex < im:
#         break
#     else:
#         n += 1
# print(n)

# ## 시간초과
# ## 21억 이하의 자연수가 입력되므로 -> 반복문으로는 해결 불가능

A, B, C = input().split()

if (int(C) - int(B)) <= 0:
    print(-1)
else:
    print(int(int(A) / (int(C) - int(B)) + 1))