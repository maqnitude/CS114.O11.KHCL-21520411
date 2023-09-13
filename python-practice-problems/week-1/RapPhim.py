import math

m, n, a = map(int, input().split())

# rounding up to ensure full floor coverage
brick_width_count = math.ceil(m / a)
brick_height_count = math.ceil(n / a)
brick_count = brick_width_count * brick_height_count

print(brick_count)