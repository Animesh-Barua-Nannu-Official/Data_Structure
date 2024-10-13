def printCLL(last):
    if last is None:
        return last
    
    temp_head = last.next

    while temp_head.next is not temp_head:
        print(temp_head.data)
        temp_head = temp_head.next
    print()