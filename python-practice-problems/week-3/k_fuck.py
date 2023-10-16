from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))

def binary_search(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

def get_k_closest(arr, k, x):
    i = binary_search(arr, x)
    l, r = i, i + 1
    for _ in range(k):
        if l < 0:
            return arr[0], arr[k - 1]
        elif r == len(arr):
            return arr[len(arr) - k], arr[-1]

        if (x - arr[l]) <= (arr[r] - x):
            l -= 1
        else:
            r += 1
    return arr[l+1], arr[r-1]

while True:
    try:
        k, x = map(int, stdin.readline().split())
        k = min(k, n)

        if x < arr[0]:
            print(arr[0], arr[k - 1])
        elif x > arr[-1]:
            print(arr[len(arr) - k], arr[-1])
        else:
            closests = get_k_closest(arr, k, x)
            print(closests[0], closests[1])
    except:
        break
