# Fly me to the Alpha Centauri

# %%
# T = int(input())
# for _ in range(T):
#     x, y = input().split()
#     n = int(y) - int(x)
#     if n == 1:
#         print(1)
#     else:
#         r = 1
#         answer = 1
#         while True:
#             if n-1 <= r:
#                 print(answer+1)
#                 break
#             answer += 1
#             r += answer


# # %%
# T = int(input())
# for _ in range(T):
#     x, y = input().split()
#     n = int(y) - int(x)
#     move = 1
#     level = 1
#     num = 1
#     while n:
#         print(num)
#         if n < num:
#             print(level)
#             break
#         if n % 2:
#             num = move
#             level += 1
#         else:
#             num += move
#             level += 1
            
        
#         n -= 1

# # %%
# T = int(input())
# for _ in range(T):
#     x, y = input().split()
#     n = int(y) - int(x)
#     answer = 0
#     key = 0
#     level = 1
#     while True:
#         for _ in range(2):
#             print(key)
#             key += level
#             if n <= key:
#                 pass
#             answer += 1
#         if n <= key:
#             print(answer)
#             break
#         level += 1
# # %%
# T = int(input())
# for _ in range(T):
#     x, y = input().split()
#     n = int(y) - int(x)
#     answer = 0
#     key = 0
#     level = 1
#     while True:
#         for _ in range(2):
#             key += level
#             if n <= key:
#                 print(answer)
#                 pass
#             else:
#                 answer += 1
#         level += 1
#         if n <= key:
#             print(answer)
#             break
# # %%
# T = int(input())
# for _ in range(T):
#     x, y = input().split()
#     n = int(y) - int(x)
#     answer = 0
#     key = 0
#     level = 1
#     while True:
#         print(key)
#         if answer % 2:   # 홀수이면
#             key += level
#             answer += 1
#             if n <= key:
#                 print(answer)
#                 break
            
#         else:            # 짝수이면
#             key += level
#             answer += 1
#             if n <= key:
#                 print(answer)
#                 break
#             level += 1
 
# %%
T = int(input())
for _ in range(T):
    x, y = input().split()
    n = int(y) - int(x)
    answer = 0
    key = 0
    level = 1
    while True:
        if answer % 2 == 0:   
            answer += 1
            key += level
            if n <= key:
                print(answer)
                break
            
        else:
            answer += 1
            key += level
            if n <= key:
                print(answer)
                break
            level += 1          ## level 더하기가 홀수 단계에서 발생해야 다음 level로 넘어갈 수 있음
# %%
