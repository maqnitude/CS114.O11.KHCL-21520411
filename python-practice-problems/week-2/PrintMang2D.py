r, c = map(int, input().split())

matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))
    
widths = [max(len(str(matrix[i][j])) for i in range(r)) for j in range(c)]

for i in range(r):
    print(' '.join(f'{matrix[i][j]:>{widths[j]}}' for j in range(c)))