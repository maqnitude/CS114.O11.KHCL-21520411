import array
from sys import stdin, stdout

def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            res = m
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return res

n = int(stdin.readline())
arr = array.array('i', map(int, stdin.readline().split()))
m = int(stdin.readline())
for x in (int(x) for x in stdin.readline().split()):
    stdout.write(str(binary_search(arr, x)))
    stdout.write('\n')
