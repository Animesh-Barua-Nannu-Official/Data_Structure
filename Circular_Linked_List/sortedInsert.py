'''
Sorted insert for circular linked list

Given a sorted Circular Linked List. The task is to insert the given data in a sorted way.

'''

from nodeCircularLL import Node

def sortedInsert(head, data):
    n_node = Node(data)

    if head is None:
        n_node.next = n_node
        return n_node

    if data <= head.data:
        last_node = head
        while last_node.next is not head:
            last_node = last_node.next
        n_node.next = head
        last_node.next = n_node
        head = n_node
        return head
    
    curr = head
    next_node = head.next

    while curr.next != head:
        if curr.data < data and next_node.data >=  data:
            n_node.next = curr.next
            curr.next = n_node
            return head
        
        else:
            curr = curr.next
            next_node = next_node.next

        n_node.next = head
        curr.next = next_node
        return head
    
