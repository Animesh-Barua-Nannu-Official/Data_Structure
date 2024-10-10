'''
Reverse a Linked List

Given a linked list, the task is to reverse the linked list by changing the links between nodes.

Examples: 

Input: Linked List = 1 -> 2 -> 3 -> 4 -> NULL 
Output: Reversed Linked List = 4 -> 3 -> 2 -> 1 -> NULL


Input: Linked List = 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
Output: Reversed Linked List = 5 -> 4 -> 3 -> 2 -> 1 -> NULL


Input: Linked List = NULL 
Output: Reversed Linked List = NULL


Input: Linked List = 1->NULL 
Output: Reversed Linked List = 1->NULL
'''

def reverseLL(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev
    return head

def reverseLLRecursive(head):
    if head is None or head.next is None:
        return head
    
    rest = reverseLLRecursive(head.next)

    head.next.next = head

    head.next = None

    return rest