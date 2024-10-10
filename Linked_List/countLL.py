'''
Find Length of a Linked List (Iterative and Recursive)

Given a Singly Linked List, the task is to find the Length of the Linked List.

Examples: 

Input: LinkedList = 1->3->1->2->1
Output: 5


Input: LinkedList = 2->4->1->9->5->3->6
Output: 7 
'''


def countNodes(head):
    '''itretive approch to find the number of nodes in an list. Parameter: head'''
    count = 0 
    temp = head

    while temp is not None:
        count += 1
        temp = temp.next
    return count

def countNodesRecursive(head):
    '''Recursive approch to find the number of nodes in an list. Parameter: head'''

    temp = head
    if temp is None:
        return 0
    return 1 + countNodesRecursive(temp.next) 