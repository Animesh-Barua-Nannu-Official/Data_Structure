from nodeCircularLL import Node

def insertEmptyList(last, data):
    if last is None:
        return None
    
    n_node = Node(data)

    n_node.next = n_node

    return n_node

def insertBegining(last, data):
    n_node = Node(data)

    if last is None:
        n_node.next = n_node
        return n_node
    
    n_node.next = last.next
    last.next = n_node

    return last

def insertEnd(last, data):
    n_node = Node(data)
    if last is None:
        last = n_node
        n_node.next = n_node
        return last
    
    n_node.next = last.next
    last.next = n_node
    last = n_node
    return last

def insertAtPosition(last, data, position):
    if last is None:
        if position != 1:
            print('invalid position')
            return last
        n_node = Node(data)
        n_node.next = n_node
        return n_node
    
    n_node = Node(data)

    head = last.next

    if position == 1:
        n_node.next = head
        last.next = n_node
        return last
    
    for i in range(1, position-1):
        head = head.next

        if head == last.next:
            print('invalid position')
            return last
    
    n_node.next = head.next
    head.next = n_node

    if head == last:
        last = n_node
        return last