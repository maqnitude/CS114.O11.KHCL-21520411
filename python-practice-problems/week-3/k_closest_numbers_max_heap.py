import heapq

n_old = int(input())
arr = list(map(int, input().split()))
n = len(arr)

def k_closest_numbers(arr, k, x):
    max_heap = []

    l = 0
    r = len(arr) - k
    while l < r:
        m = (l + r) // 2

        if arr[m] < x:
            l = m + 1
        else:
            r = m
    
    for num in arr[max(l - k, 0):min(l + k, len(arr))]:
        heapq.heappush(max_heap, (-abs(num - x), -num))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # return -min(max_heap, key=lambda item: -item[1])[1], -max(max_heap, key=lambda item: -item[1])[1]
    return -min(max_heap, key=lambda item: -item[1])[1], -max_heap[0][1]

while True:
    temp = input()
    if temp == "":
        break;

    k, x = map(int, temp.split())

    if x <= arr[0]:
        print(arr[0], arr[k - 1])
    elif x >= arr[-1]:
        print(arr[n - k], arr[n - 1])
    else:
        closest_numbers = k_closest_numbers(arr, k, x)
        print(closest_numbers[0], closest_numbers[1])
