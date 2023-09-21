n = int(input())
a = list(map(int, input().split()))

a_max_removed = [ele for ele in a]
a_max_removed.remove(max(a_max_removed))

a_min_removed = [ele for ele in a]
a_min_removed.remove(min(a_min_removed))

stability_max_removed = max(a_max_removed) - min(a_max_removed)
stability_min_removed = max(a_min_removed) - min(a_min_removed)

print(min(stability_max_removed, stability_min_removed))