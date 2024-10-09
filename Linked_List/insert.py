from print import printLL

class Node:
    '''Node class for singly linked list'''
    def __init__(self, data=None):
        self.next = None
        self.data = data

def insertBeforeHead(head, new_data):
    '''insert a Node before head node'''
    n_node = Node(new_data) #creating new node
    n_node.next = head # pointing to head node
    head = n_node #making new head node
    return head

def insertAfter(head, given_key, new_data):
    '''insert a node after a node with particular key'''
    temp = head

    while temp is not None:
        if temp.data == given_key:
            break
        temp = temp.next
    
    if temp == None:
        return 'given key is not present'
    
    n_node = Node(new_data)
    n_node.next = temp.next
    temp.next = n_node
    return head

def insertBefore(head, given_key, new_data):
    '''insert a node before a node with particular key'''
    temp = head
    #if list is empty
    if head == None:
        return None
    
    #if the key is in the head. Then it will be the new head
    if temp.data == given_key:
        head = insertBeforeHead(head, given_key)
        return head
    
    #for other cases
    while temp is not None:
        if temp.next.data == given_key:
            break
        temp = temp.next

    if temp is not None:
        n_node = Node(new_data)
        n_node.next = temp.next
        temp.next = n_node
    return head

def insertPosition(head, position, new_data):
    '''insert a node at a particulart position where position start from 1'''
    n_node = Node(new_data)

    if position == 1:
        n_node.next = head
        head = n_node
        return head
    
    temp = head
    for _ in range(1, position-1):
        if temp == None:
            break
        temp = temp.next

    if temp is None:
        print('Position is out of bound')
        return head
    
    n_node.next = temp.next
    temp.next = n_node
    return head

def insertEnd(head, new_data):
    '''inserting at the end of a liked list'''
    if head == None:
        return None
    
    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = Node(new_data)
    return head


    



if __name__ == "__main__":
  
    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    data = 1
    head = insertBeforeHead(head, data)

    printLL(head)

    key = 3
    newData = 4
    head = insertAfter(head, key, newData)

    printLL(head)

    newData = 6
    key = 2

    head = insertBefore(head, key, newData)

    printLL(head)