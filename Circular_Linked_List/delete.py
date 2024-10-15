from nodeCircularLL import Node

def deleteFirstNode(last):
    '''
    delete the first node of a linked list. param: last -> last node
    '''
    if last is None:
        print('Empty list')
        return None
    
    head = last.next

    if head == last:
        last = None

    else:
        last.next = head.next

    return last

def deleteSpecificNode(last, key):
    '''
    delete the node of the Linked list with given key. param: last, key
    '''
    if last is None:
        print('List is empty.')
        return None
    
    curr = last.next
    prev = last

    # if only one node exist
    if last == curr and curr.data == key:
        last = None
        return None
    
    #if head/curr is has the key
    if curr.data == key:
        last.next = curr.next
        return last
    
    #for other cases
    while curr != last:
        if curr.data == key:
            break
        prev = curr
        curr = curr.next

    if curr.data == key:
        prev.next = curr.next
        if curr == last:
            last = prev

    else:
        print('Node is not found')
    return last

def deleteLastNode(last):
    '''
    delete the last of the linked list: param: last
    '''
    if last is None:
        print('List is empty.')
        return None
    
    head = last.next

    if head == last:
        last = None
        return last
    
    curr = head
    while curr.next is not last:
        curr = curr.next

    curr.next = head
    last = curr
    return last

