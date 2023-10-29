#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaf_values):
            if not node:
                return
            if not node.left and not node.right:
                leaf_values.append(node.val)
            dfs(node.left, leaf_values)
            dfs(node.right, leaf_values)
        
        seq1 = []
        dfs(root1, seq1)
        seq2 = []
        dfs(root2, seq2)
        
        return seq1 == seq2
        
# @lc code=end

