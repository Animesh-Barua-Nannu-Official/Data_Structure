'''
Print a given matrix in spiral form

Given an m x n matrix, the task is to print all elements of the matrix in spiral form.

Examples: 

 Input: matrix = {{1,    2,   3,   4},
                             {5,    6,   7,   8},
                            {9,   10,  11,  12},
                           {13,  14,  15,  16 }}
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
Explanation: The output is matrix in spiral format.
'''
def spiralPrint(m, n, a):
    top, bottom, left, right = 0, m - 1, 0, n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(a[top][i], end=" ")
        top += 1

        for i in range(top, bottom + 1):
            print(a[i][right], end=" ")
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(a[bottom][i], end=" ")
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(a[i][left], end=" ")
            left += 1
