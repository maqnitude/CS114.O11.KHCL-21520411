n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

# To rotate any square matrix by 90 degrees clockwise:
#   Transpose the matrix
#   Reverse every row
def rotate_cw90(matrix):
    # Transpose
    matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
    # Reverse every row
    matrix = [matrix[i][::-1] for i in range(n)]
    
    return matrix

def compare(matrix_a, matrix_b):
    for i in range(n):
        for j in range(n):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False
    return True

A_cw90 = rotate_cw90(A)
A_cw180 = rotate_cw90(A_cw90)
A_cw270 = rotate_cw90(A_cw180)
A_cw360 = rotate_cw90(A_cw270)

if compare(A_cw90, B) or compare(A_cw180, B) or compare(A_cw270, B) or compare(A_cw360, B):
    print('YES')
else:
    print('NO')