'''
A Boolean Matrix Question

Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1. 

Examples:

Input: {{1, 0},
           {0, 0}}
Output: {{1, 1}
              {1, 0}}
Input: {{0, 0, 0},
            {0, 0, 1}}
Output: {{0, 0, 1},
               {1, 1, 1}}
 


Input: {{1, 0, 0, 1},
        {0, 0, 1, 0},
        {0, 0, 0, 0}}
Output: {{1, 1, 1, 1},
               {1, 1, 1, 1},
              {1, 0, 1, 1}}


'''


def boolMatrix(mat, n, m):
    row = [0]*n
    col = [0]*m
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                row[i] = 1
                col[j] = 1
    
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j]== 1:
                mat[i][j] = 1
                
