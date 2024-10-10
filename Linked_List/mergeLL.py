'''
Merge two sorted linked lists

Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the lists (in place) and return the head of the merged list.

Examples:

Input: a: 5->10->15,  b: 2->3->20
Output: 2->3->5->10->15->20


Input: a: 1->1, b: 2->4
Output: 1->1->2->4

Input: a: 1->2->3, b: null
Output: 1->2->3
'''

def mergeSortedList(a, b):
    result = None

    if a is None:
        return b
    elif b is None:
        return a
    
    if a.data <= b.data:
        result = a
        result.next = mergeSortedList(a.next, b)
    else:
        result = b
        result.next = mergeSortedList(a, b.next)

#Iteratively merges two lists sorted in increasing order
def mergeSortedLists(a, b):
    if a is None:
        return a
    elif b is  None:
        return b
    
    head = None
    tail = None

    if a.data <= b.data:
        head = tail = a
        a = a.next
    else:
        head = tail = b
        b = b.next

    #merge the remaining nodes

    while a and b:
        if a.data <= b.data:
            tail.next = a
            tail = a
            a  = a.next
        else:
            tail.next = b
            tail = b
            b = b.next

    #Attach the remaining part of the list that not yet exhausted
    if a is None:
        tail.next = b
    elif b is None:
        tail.next = a

    return head

    
