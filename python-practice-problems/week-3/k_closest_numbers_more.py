import sys

n_old = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))
n = len(arr)

# Use binary search to search for the starting point of the subarray
def k_closest_numbers(arr, len_arr, k, x):
    len_arr = len(arr)
    if x <= arr[0]:
        return arr[0], arr[k - 1]
    elif x >= arr[-1]:
        return arr[len_arr - k], arr[-1]

    l = 0
    r = len_arr - k
    while l < r:
        m = (l + r) // 2

        # if k elements after arr[m] are closer to x then
        # the starting point must be to the right of arr[m]
        if abs(arr[m] - x) > abs(arr[m + k] - x):
            l = m + 1
        else:
            r = m

    return arr[l], arr[l + k - 1]

while True:
    temp = sys.stdin.readline()
    if temp == '\n':
        break

    k, x = map(int, temp.split())

    closest_numbers = k_closest_numbers(arr, n, k, x)
    sys.stdout.write(str(closest_numbers[0]) + ' ' + str(closest_numbers[1]) + '\n')
