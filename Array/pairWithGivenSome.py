'''
Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target. This problem is a variation of 2Sum problem.

Examples:

Input: arr[] = {0, -1, 2, -3, 1}, target = -2
Output: True
Explanation: If we calculate the sum of the output,1 + (-3) = -2


Input: arr[] = {1, -2, 1, 0, 5}, target = 0
Output: False
'''

def pairWithGivenSome(arr, target):
    left = 0
    right = len(arr)-1
    sum=0
    arr.sort()
    while left<right:
        sum = arr[left]+arr[right]
        if sum == target:
            return True
        elif sum>target:
            right -= 1
        elif sum< target:
            left += 1
    return False

if __name__ == "__main__":
    print(pairWithGivenSome([0, -1, 2, -3, 1], -2))
    print(pairWithGivenSome([1, -2, 1, 0, 5], 0))