#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cahce = {} # map key to node
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cahce:
            self.remove(self.cahce[key])
            self.insert(self.cahce[key])
            return self.cahce[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cahce:
            self.remove(self.cahce[key])
        self.cahce[key] = Node(key, value)
        self.insert(self.cahce[key])
        
        if len(self.cahce) > self.cap:
            # remove from the list and delete from the map
            node = self.left.next
            self.remove(node)
            del self.cahce[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

