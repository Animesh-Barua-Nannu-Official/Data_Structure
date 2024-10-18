'''
Deletion in a Doubly Linked List

Deleting a node in a doubly linked list is very similar to deleting a node in a singly linked list. However, there is a little extra work required to maintain the links of both the previous and next nodes. In this article, we will learn about different ways to delete a node in a doubly linked list.

Example:

Input: DLL = 1 <-> 2 <->3 , Node = 1
Output:  2 <-> 3


Input: DLL = 2 <-> 45 <-> 3 <-> 1, Node = 45
Output:  2 <-> 3<-> 1
'''

def delHead(head):
    '''
    deleting the head
    param: head
    return: head
    '''
    if head is None:
        return None

    head = head.next

    if head is not None:
        head.prev = None
    return head

def delAfter(head, key):
    curr = head

    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    if curr is None or curr.next is None:
        return head
    
    del_node = curr.next

    curr.next = del_node.next

    if del_node.next is not None:
        del_node.next.prev = curr
    return head

def delBefore(head, key):
    '''
    delete before the given key
    param: head, key
    return: head
    '''
    curr = head

    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    if curr is None or curr.prev is None:
        return head

    del_node = curr.prev

    curr.prev = del_node.prev

    if del_node.prev is not None:
        del_node.prev.next = curr
    else:
        head = curr

    return head

def delAtPosition(head, pos):
    if head is None:
        return head

    curr = head

    for _ in range(1, pos):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head
    
    if curr.prev is not None:
        curr.prev.next = curr.next

    if curr.next is not None:
        curr.next.prev = curr.prev

    if head == curr:
        head = curr.next

    return head

def delEnd(head):
    if (head is None) or (head.next is None):
        return None
    curr = head
    while curr.next is not None:
        curr = curr.next

    if curr.prev is not None:
        curr.prev.next = None

    return head
    
