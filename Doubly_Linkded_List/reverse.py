'''
Reverse a Doubly Linked List

Given a Doubly Linked List, the task is to reverse the Doubly Linked List.

Examples:

Input: Doubly Linked List = 1 <-> 2 <-> 3 -> NULL 
Output: Reversed Doubly Linked List = 3 <-> 2 <-> 1 -> NULL
'''

def reverseRecursive(head):
    '''
    reverse using recurssion 
    '''
    if head is None:
        return None
    
    temp = head.next
    head.next = head.prev
    head.prev = temp

    if head.prev is None:
        return head
    
    return reverseRecursive(head.prev)

def reverse(head):
    '''
    reverse using pointers
    '''
    if head is None or head.next is None :
        return head
    
    prevNode = None
    currNode = head

    while currNode is not None:
        prevNode = currNode.prev
        currNode.prev = currNode.next
        currNode.next = prevNode

        currNode = currNode.prev

    return prevNode.prev
