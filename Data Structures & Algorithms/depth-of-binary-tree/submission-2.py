# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        IDEA: use recursive DFS with a depth tracker on each
        1. edge case if root none return 0
        2. return 1+

        '''

        if root is None:
            return 0

        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))