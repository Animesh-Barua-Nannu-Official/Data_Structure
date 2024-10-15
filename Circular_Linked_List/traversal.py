from nodeCircularLL import Node

def printCLLrecursive(curr, head):
    if head is None:
        return
    print(curr.data, end = ' ')

    if curr.next ==head:
        return
    printCLLrecursive(curr.next, head)

def printCLLitretive(last):
    if last is None:
        print('List is  empty')
        return last
    curr = last.next

    while curr.next is not curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()

if __name__ == "__main__":
  
      
    # Create a hard-coded linked list
    # 11 -> 2 -> 56 -> 12
    head = Node(11)
    head.next = Node(2)
    head.next.next = Node(56)
    head.next.next.next = Node(12)
    last = head.next.next.next
    last.next = head

    printCLLitretive(last)
