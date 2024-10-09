'''
Given an array arr[] of size n, the task is to print all the Leaders in the array. An element is a Leader if it is greater than all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

Input: arr[] = {16, 17, 4, 3, 5, 2}
Output: 17 5 2
Explanation: 17 is greater than all the elements to its right: 4, 3, 5 and 2, therefore 17 is a leader. 5 is greater than all the elements to its right: 2, therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.


Input: arr[] = {1, 2, 3, 4, 5, 2}
Output: 5 2
Explanation: 5 is greater than all the elements to its right: 2, therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
'''

def leader(arr):
    last_lead = -10000000000
    arr2 = []
    for i in range(len(arr)-1, -1, -1):
        if arr[i]>=last_lead:
            arr2.append(arr[i])
            last_lead = arr[i]
    return arr2

if __name__ == "__main__":
    print(leader([16, 17, 4, 3, 5, 2]))
    print(leader([1, 2, 3, 4, 5, 2]))
