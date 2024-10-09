def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=' ')
        temp = temp.next
    print()
