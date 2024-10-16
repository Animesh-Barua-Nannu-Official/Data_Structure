from nodeDoubly import Node

def insertFront(head, data):
    '''
    insertion in the head node
    param: head, data
    return: head
    '''
    new_node = Node(data)

    new_node.next = head

    if head is not None:
        head.prev = new_node

    head = new_node
    return head

def insertAfter(head, key,data):
    '''
    insertion after given node
    param: head, key, data
    return: head
    '''
    temp = head

    while temp is not None:
        if temp.data == key:
            break
        temp = temp.next

    if temp is None:
        return head
    
    new_node = Node(data)
    new_node.prev = temp
    new_node.next = temp.next

    temp.next = new_node

    if new_node.next is  None:
        new_node.next.prev = new_node

    return head

def insertBefore(head, key, data):
    '''
    insertion before a given node
    param: head, key, data
    return: head
    '''
    temp = head

    while temp is not None:
        if temp.data == key:
            break
        temp = temp.next

    if temp is None:
        return head
    
    new_node = Node(data)
    new_node.prev = temp.prev
    new_node.next = temp

    if temp.prev is not None:
        temp.prev.next = new_node
    else:
        head = new_node

    temp.prev = new_node
    return head

def insertAtPosition(head, pos, data):
    new_node = Node(data)

    if pos == 1:
        new_node.next  = head

        if head is not None:
            head.prev = new_node

        head = new_node
        return head
    
    curr = head
    for _ in range(1, pos - 1):
        if curr is None:
            print('Position is out of bound')
            return head
        curr = curr.next

    if curr is None:
        print('Position is out of bound')
        return head
    new_node.prev = curr

    new_node.next = curr.next

    curr.next = new_node

    if new_node.next is not None:
        new_node.next.prev = new_node
    return head

def insertEnd(head, data):
    '''
    insertion at the end
    param: head, data
    return: head
    '''
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr
    return head
