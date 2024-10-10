'''
Given a singly linked list with two values x and y, the task is to swap two nodes having values x and y without swapping data.

Examples: 

Input: 1->2->3->4->5, x = 2, y = 4
Output: 1->4->3->2->5

'''

from insert import Node

def swapNodes(head, x, y):
    if x == y:
        return head
    
    prevX = None
    currX = None
    prevY = None
    currY = None

    prev = None
    curr = head

    while curr is not None:
        if curr.data == x:
            prevX = prev
            currX = curr
        elif curr.data == y:
            prevY = prev
            currX = curr
        prev = curr
        curr = curr.next

    if currX == None or currY == None:
        return head
    
    if prevX is not None:
        prevX.next = currY
    else:
        head = currY

    if prevY is not None:
        prevY.next = currX
    else:
        head =  currX

    temp = currY.next
    currY.next = currX.next
    currX.next = temp

    return head