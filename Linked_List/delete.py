from print import printLL

class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

def deleteBegining(head):
    '''removing the first node of a list. So updating the head to next node'''
    if head is None:
        return head
    temp = head
    head = temp.next
    del temp
    return head

def deleteNode(head, position):
    '''deleting a node from the middle of a list'''
    temp = head
    prev = None
    #if head is empty
    if head is None:
        return head
    #if deleting node is head node  
    if position == 1:
        return deleteBegining(head)
    #if deleting node is on the middle
    for _ in range(1, position):
        prev = temp
        temp = temp.next
        if temp is None:
            print("Data not presetn")
            return head
        
    prev.next = temp.next
    return head

def deleteLastNode(head):
    '''deleting the last node of the linked list'''
    if head is None:
        return None
    if head.next is None:
        return None
    
    prev = None
    temp = head
    while temp.next is not None:
        prev = temp
        temp = temp.next

    prev.next = None
    return head

def deleteNodekey(head, key):
    '''deleting a node with givnen value'''
    temp = head
    if head is None:
        return None
    if key == head.data:
        head = head.next
        return head
    
    while temp is not None:
        if temp.next.data == key:
            break
        temp = temp.next
    if temp is not None:
        d_node = temp.next
        temp.next = d_node.next
    return head


if __name__ == "__main__":

    # Creating a linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ")
    printLL(head)
    # Deleting the head node
    head = deleteBegining(head)
    print("List after deleting the head: ")
    printLL(head)

