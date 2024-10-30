'''
Search in a row wise and column wise sorted matrix

Given an N X N matrix and an integer X, find the position of X in the matrix if it is present. Otherwise, print “Element not found”. Every row and column of the matrix is sorted in increasing order.

Examples: 

Input: mat[4][4] = { {10, 20, 30, 40},  X = 29
                               {15, 25, 35, 45},
                               {27, 29, 37, 48},
                             {32, 33, 39, 50}}
 
Output: Found at (2, 1)
Explanation: Element at (2,1) is 29


Input : mat[4][4] = { {10, 20, 30, 40},   X = 100
                                {15, 25, 35, 45},
                               {27, 29, 37, 48},
                              {32, 33, 39, 50}};
     
Output: Element not found
Explanation: Element 100 does not exist in the matrix

'''
import numpy as np

def searchInSortedMatrix(x, mat):
    '''my solution'''
    row, col = mat.shape
    arr = None
    index_x = None
    for i in range(row):
        if mat[i][0]<=x and mat[i][col-1]>=x:
            arr = mat[i]
            index_x = i
    index_y = None
    for j in range(len(arr)):
        if arr[j]==x:
            index_y = j
        
    if index_y is None:
        return 'not found'

    return index_x, index_y

def search(mat, n, x):
    row = 0
    col = n-1
    while (row<n and col>=0):
        if mat[row][col] == x:
            return row, col
        if mat[row][col]>x:
            col -= 1
        else:
            row += 1

    if row == n or col == -1:
        return None


mat = np.array([[10, 20, 30, 40], 
                [15, 25, 35, 45],
                [27, 29, 37, 48],
                [32, 33, 39, 50]])

print(searchInSortedMatrix(29, mat))