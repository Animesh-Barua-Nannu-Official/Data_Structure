'''
Split a Circular Linked List into two halves

Given a Circular linked list. The task is split into two Circular Linked lists. If there are an odd number of nodes in the given circular linked list then out of the resulting two halved lists, the first list should have one node more than the second list.

Examples:

Input:  10->4->9
Output: 10->4 , 9
Explanation: Number of nodes in circular Linked List are odd, so it will split as shown below.
'''

def splitList(head):
    slow_tor = head
    fast_hare = head

    if head is None:
        return None, None

    while fast_hare.next != head and fast_hare.next.next != head:
        fast_hare = fast_hare.next.next
        slow_tor = slow_tor.next

    if fast_hare.next.next == head:
        fast_hare = fast_hare.next
    
    head1 = head

    head2 = slow_tor.next

    fast_hare.next = slow_tor.next

    slow_tor.next = head

    return head1, head2