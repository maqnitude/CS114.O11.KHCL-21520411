n = int(input())
arr = list(map(int, input().split()))
k, x = map(int, input().split())

def get_distance(number):
    return abs(number - x)

print(" ".join(map(str, sorted(sorted(arr, key=get_distance)[:k]))))
