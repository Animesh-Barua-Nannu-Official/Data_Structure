'''
Given an array arr. Find the majority element in the array. If no majority exists, return -1. A majority element in an array is an element that appears strictly more than arr.size() / 2 times in the array.

Examples : 

Input : arr[] = {1, 1, 2, 1, 3, 5, 1}
Output : 1
Explanation: Note that 1 appear 4 times which is more than  7 / 2 times 


Input : arr[] = {3, 3, 4, 2, 4, 4, 2, 4}
Output :  -1 
Explanation: There is no element whose frequency is greater than the half of the size of the array size.


Input : arr[] = {3}
Output : 3
Explanation: Appears more than n/2 times
'''

def majority_element(arr):
    n = len(arr)
    candidate = -1
    count = 0

    # Find a candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Validate the candidate
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    # If count is greater than n / 2, return the candidate; otherwise, return -1
    if count > n // 2:
        return candidate
    else:
        return -1