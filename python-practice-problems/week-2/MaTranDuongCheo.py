n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

def is_diagonal_matrix(matrix):
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][j] != 1:
                return 'NO'
            if i != j and matrix[i][j] != 0:
                return 'NO'
    return 'YES'

print(is_diagonal_matrix(mat))