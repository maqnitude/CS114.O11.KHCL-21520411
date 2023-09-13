k, t = map(int, input().split())

if t <= k:
    print(t)
else:
    if (t // k) % 2 == 0:   # going to station k
        print(t % k)
    else:                   # going to station 0
        print(k - (t % k))