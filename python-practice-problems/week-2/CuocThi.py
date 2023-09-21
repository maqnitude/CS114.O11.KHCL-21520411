n, k = map(int, input().split())
a = list(map(int, input().split()))

score_required = a[k - 1]
team_count = 0
for i in range(n):
    if a[i] >= score_required and a[i] > 0:
        team_count += 1

print(team_count)