class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)
    last = Node(4)

    # circular linked list
    head = first
    first.next = second
    second.next = third
    third.next = last
    last.next = first