def search(last, key):
    '''
    search a key in linked list. param: last, key . return: True/False
    '''
    if last is None:
        return False
    
    head = last.next
    curr = head

    while curr != last:
        if curr.data == key:
            return True
        curr = curr.next
    
    if last.data == key:
        return True
    
    return False