# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# Implementation of Singly Linked List
class LinkedList:
    # initialize the linked list with head and tail
    def __init__(self):
        #  create a dummy head
        self.head = ListNode(-1)
        self.tail = self.head
    # get the element at index i
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
    # set the element at index i to n
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
    # push back the element n to the linked list
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
    # pop back the last element in the linked list
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        # if the index is valid
        if curr and curr.next:
            # if the node to be removed is the tail
            if curr.next == self.tail:
                self.tail = curr
            # remove the node
            curr.next = curr.next.next
            return True
        return False
    # get the size of the linked list
    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res