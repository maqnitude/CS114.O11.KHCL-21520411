n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

# Only 1 of the 2 diagonals is allowed to have all 1s
# Check the primary diagonal first, then the secondary one
# Lastly check the remaining elements
def check(matrix):
    valid_primary_diagonal = True

    # check primary diagonal
    for i in range(n):
        if matrix[i][i] != 1:
            valid_primary_diagonal = False
            break

    if not valid_primary_diagonal: # check secondary diagonal
        for i in range(n):
            j = n - 1 - i
            if matrix[i][j] != 1:
                return 'NO'
    
    if valid_primary_diagonal:
        for i in range(n):
            for j in range(n):
                if i != j and matrix[i][j] != 0:
                    return 'NO'
    else:
        for i in range(n):
            k = n - 1 - i
            for j in range(n):
                if j != k and matrix[i][j] != 0:
                    return 'NO'
    
    return 'YES'

print(check(mat))