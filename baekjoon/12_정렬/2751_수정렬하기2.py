# 수 정렬하기 2

#%%
N = int(input())
answer = [int(input()) for i in range(N)]

#%%
## 병합 정렬 -> merge sort

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    m = len(unsorted_list) // 2
    left = unsorted_list[:m]
    right = unsorted_list[m:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)

    return merge(left1, right1)

def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    while (i < len(left)) & (j < len(right)):       ## and 아니라 & 사용해야 함
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while (i < len(left)):
        sorted_list.append(left[i])
        i += 1
    
    while (j < len(right)):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

for i in merge_sort(answer):
    print(i)


# %%
## 힙 정렬
def heap(li, idx, n):
    l = idx * 2
    r = idx * 2 + 1
    s_idx = idx
    if (l <= n and li[s_idx] > li[l]):
        s_idx = l
    if (r <= n and li[s_idx] > li[r]):
        s_idx = r
    if s_idx != idx:
        li[idx], li[s_idx] = li[s_idx], li[idx]
        return heap(li, s_idx, n)

def heap_sort(v):
    n = len(v)
    v = [0] + v # 인덱스 1부터 시작하기 위해 가장 앞에 0 추가
    
    for i in range(n, 0, -1):
        heap(v, i, n)

    for i in range(n, 0, -1):
        print(v[1])
        v[i], v[1] = v[1], v[i]
        heap(v, 1, i-1)

heap_sort(answer)
#%%